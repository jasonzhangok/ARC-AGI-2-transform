from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    separator_row = next(r for r, row in enumerate(grid) if len(set(row)) == 1)
    separator_color = grid[separator_row][0]
    separator_col = next(c for c in range(width) if all(grid[r][c] == separator_color for r in range(height)))
    ranges = [
        (0, separator_row, 0, separator_col),
        (0, separator_row, separator_col + 1, width),
        (separator_row + 1, height, 0, separator_col),
        (separator_row + 1, height, separator_col + 1, width),
    ]
    background = Counter(
        value for row in grid for value in row if value != separator_color
    ).most_common(1)[0][0]
    for top, bottom, left, right in ranges:
        if any(grid[r][c] != background for r in range(top, bottom) for c in range(left, right)):
            return [row[left:right] for row in grid[top:bottom]]
