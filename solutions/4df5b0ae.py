from collections import Counter


def transform(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]

    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    seen = set()
    objects = []

    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color == background or (row, col) in seen:
                continue

            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = current_row + row_step
                    next_col = current_col + col_step
                    if (0 <= next_row < height and 0 <= next_col < width
                            and (next_row, next_col) not in seen
                            and grid[next_row][next_col] == color):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))

            cell_set = set(cells)
            perimeter = (
                [(0, c) for c in range(width)]
                + [(height - 1, c) for c in range(width)]
                + [(r, 0) for r in range(1, height - 1)]
                + [(r, width - 1) for r in range(1, height - 1)]
            )
            if all(cell in cell_set for cell in perimeter):
                continue

            min_row = min(r for r, _ in cells)
            max_row = max(r for r, _ in cells)
            min_col = min(c for _, c in cells)
            max_col = max(c for _, c in cells)
            normalized = [(r - min_row, c - min_col) for r, c in cells]
            objects.append((len(cells), min_row, min_col, color,
                            max_row - min_row + 1, max_col - min_col + 1,
                            normalized))

    objects.sort(key=lambda item: item[:3])
    output = [[background] * width for _ in range(height)]
    left = 0
    for _, _, _, color, object_height, object_width, cells in objects:
        top = height - object_height
        for row, col in cells:
            output[top + row][left + col] = color
        left += object_width

    return output
