from collections import Counter, defaultdict


def _perimeter(top, bottom, left, right):
    cells = [(top, col) for col in range(left, right + 1)]
    cells += [(bottom, col) for col in range(left, right + 1)]
    cells += [(row, left) for row in range(top + 1, bottom)]
    cells += [(row, right) for row in range(top + 1, bottom)]
    return cells


def _edge_directions(row, col, rectangle):
    top, bottom, left, right = rectangle
    directions = []
    if row == top:
        directions.append((-1, 0))
    if row == bottom:
        directions.append((1, 0))
    if col == left:
        directions.append((0, -1))
    if col == right:
        directions.append((0, 1))
    return directions


def _inside(rectangle, point):
    top, bottom, left, right = rectangle
    row, col = point
    return top <= row <= bottom and left <= col <= right


def _rectangles(grid, color, background):
    """Recover the largest near-solid horizontal and vertical rectangles."""
    height, width = len(grid), len(grid[0])
    candidates = []

    for top in range(height - 2):
        for bottom in range(top + 2, height):
            for left in range(width - 2):
                for right in range(left + 2, width):
                    rectangle = (top, bottom, left, right)
                    rectangle_height = bottom - top + 1
                    rectangle_width = right - left + 1
                    if rectangle_height == rectangle_width:
                        continue
                    if not all(
                        grid[row][col] == color
                        for row in range(top + 1, bottom)
                        for col in range(left + 1, right)
                    ):
                        continue

                    boundary = _perimeter(*rectangle)
                    gaps = [
                        point
                        for point in boundary
                        if grid[point[0]][point[1]] != color
                    ]
                    if any(grid[row][col] != background for row, col in gaps):
                        continue
                    if any(
                        abs(row - other_row) + abs(col - other_col) == 1
                        for index, (row, col) in enumerate(gaps)
                        for other_row, other_col in gaps[index + 1 :]
                    ):
                        continue

                    valid = True
                    for side, d_row, d_col in (
                        ([(top, col) for col in range(left, right + 1)], -1, 0),
                        ([(bottom, col) for col in range(left, right + 1)], 1, 0),
                        ([(row, left) for row in range(top, bottom + 1)], 0, -1),
                        ([(row, right) for row in range(top, bottom + 1)], 0, 1),
                    ):
                        exposed_gaps = [
                            (row, col)
                            for row, col in side
                            if grid[row][col] == background
                            and 0 <= row + d_row < height
                            and 0 <= col + d_col < width
                            and grid[row + d_row][col + d_col] == background
                        ]
                        if len(exposed_gaps) > 1:
                            valid = False
                            break

                    if not valid or any(
                        not any(
                            0 <= row + d_row < height
                            and 0 <= col + d_col < width
                            and grid[row + d_row][col + d_col] == background
                            for d_row, d_col in _edge_directions(
                                row, col, rectangle
                            )
                        )
                        for row, col in gaps
                    ):
                        continue
                    candidates.append(rectangle)

    selected = []
    for horizontal in (True, False):
        oriented = [
            rectangle
            for rectangle in candidates
            if (
                rectangle[3] - rectangle[2]
                > rectangle[1] - rectangle[0]
            )
            == horizontal
        ]
        if oriented:
            selected.append(
                max(
                    oriented,
                    key=lambda rectangle: (rectangle[1] - rectangle[0] + 1)
                    * (rectangle[3] - rectangle[2] + 1),
                )
            )
    return selected


def _isolated_along_edge(grid, row, col, direction, color, background):
    height, width = len(grid), len(grid[0])
    d_row, d_col = direction
    beyond_row = row + d_row
    beyond_col = col + d_col
    if (
        0 <= beyond_row < height
        and 0 <= beyond_col < width
        and grid[beyond_row][beyond_col] != background
    ):
        return False
    tangent = (d_col, -d_row)
    for sign in (-1, 1):
        next_row = row + sign * tangent[0]
        next_col = col + sign * tangent[1]
        if 0 <= next_row < height and 0 <= next_col < width:
            if grid[next_row][next_col] == color:
                return False
    return True


def transform(grid):
    """Mirror isolated edge signals across two overlapping solid rectangles."""
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    result = [row[:] for row in grid]

    for color in {value for row in grid for value in row if value != background}:
        rectangles = _rectangles(grid, color, background)
        events = defaultdict(set)

        for rectangle in rectangles:
            top, bottom, left, right = rectangle
            for row, col in _perimeter(*rectangle):
                for d_row, d_col in _edge_directions(row, col, rectangle):
                    opposite = (
                        row - d_row * (bottom - top),
                        col - d_col * (right - left),
                    )
                    outside = (row + d_row, col + d_col)

                    if (
                        grid[row][col] == background
                        and 0 <= outside[0] < height
                        and 0 <= outside[1] < width
                        and grid[outside[0]][outside[1]] == background
                    ):
                        target = (
                            opposite[0] - d_row,
                            opposite[1] - d_col,
                        )
                        if 0 <= target[0] < height and 0 <= target[1] < width:
                            events[("gap", (row, col))].add(
                                (rectangle, opposite, target, color)
                            )
                    elif (
                        0 <= outside[0] < height
                        and 0 <= outside[1] < width
                        and grid[outside[0]][outside[1]] == color
                        and _isolated_along_edge(
                            grid,
                            outside[0],
                            outside[1],
                            (d_row, d_col),
                            color,
                            background,
                        )
                    ):
                        events[("bump", outside)].add(
                            (rectangle, opposite, opposite, background)
                        )

        for hypotheses in events.values():
            owners = hypotheses
            if len({hypothesis[0] for hypothesis in hypotheses}) > 1:
                cover_counts = {
                    hypothesis: sum(
                        other != hypothesis[0]
                        and _inside(other, hypothesis[1])
                        for other in rectangles
                    )
                    for hypothesis in hypotheses
                }
                least_covered = min(cover_counts.values())
                owners = {
                    hypothesis
                    for hypothesis in hypotheses
                    if cover_counts[hypothesis] == least_covered
                }

            for _, _, target, value in owners:
                result[target[0]][target[1]] = value

    return result
