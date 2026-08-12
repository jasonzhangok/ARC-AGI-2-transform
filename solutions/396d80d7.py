from collections import Counter


def _runs(indices):
    """Return the inclusive endpoints of consecutive integer runs."""
    if not indices:
        return []
    runs = []
    start = previous = indices[0]
    for index in indices[1:]:
        if index != previous + 1:
            runs.append((start, previous))
            start = index
        previous = index
    runs.append((start, previous))
    return runs


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    occupied = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] != background
    ]
    if not occupied:
        return [row[:] for row in grid]

    top = min(row for row, _ in occupied)
    bottom = max(row for row, _ in occupied)
    left = min(col for _, col in occupied)
    right = max(col for _, col in occupied)

    boundary_colors = {
        grid[row][col]
        for row, col in occupied
        if row in (top, bottom) or col in (left, right)
    }
    colors = {grid[row][col] for row, col in occupied}
    central_candidates = colors - boundary_colors
    center_row = (top + bottom) / 2
    center_col = (left + right) / 2

    def centrality(color):
        points = [(r, c) for r, c in occupied if grid[r][c] == color]
        return sum(
            (r - center_row) ** 2 + (c - center_col) ** 2
            for r, c in points
        ) / len(points)

    central_color = min(central_candidates or colors, key=centrality)
    scaffold_colors = colors - {central_color}
    horizontal = set()
    vertical = set()

    # Project every horizontal scaffold segment one row away from the center.
    for row in range(top, bottom + 1):
        new_row = row + (-1 if row < center_row else 1)
        if not 0 <= new_row < height:
            continue
        cells = [
            col for col in range(left, right + 1)
            if grid[row][col] in scaffold_colors
        ]
        for start, end in _runs(cells):
            for col in (start - 1, end + 1):
                if (0 <= col < width and
                        grid[new_row][col] == background):
                    horizontal.add((new_row, col))

    # Do the rotationally symmetric construction for vertical segments.
    for col in range(left, right + 1):
        new_col = col + (-1 if col < center_col else 1)
        if not 0 <= new_col < width:
            continue
        cells = [
            row for row in range(top, bottom + 1)
            if grid[row][col] in scaffold_colors
        ]
        for start, end in _runs(cells):
            for row in (start - 1, end + 1):
                if (0 <= row < height and
                        grid[row][new_col] == background):
                    vertical.add((row, new_col))

    # A projection is part of the new outer layer if it crosses its relevant
    # side of the old box, or if both orthogonal views independently imply it.
    additions = {
        point for point in horizontal
        if point[0] < top or point[0] > bottom
    }
    additions |= {
        point for point in vertical
        if point[1] < left or point[1] > right
    }
    additions |= horizontal & vertical

    result = [row[:] for row in grid]
    for row, col in additions:
        result[row][col] = central_color

    return result
