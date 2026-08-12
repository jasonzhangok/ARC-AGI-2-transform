from collections import Counter


def transform(grid):
    counts = Counter(value for row in grid for value in row)
    border_color = next(color for color, count in counts.items() if count == 24)
    cells = [
        (row, col)
        for row, line in enumerate(grid)
        for col, value in enumerate(line)
        if value == border_color
    ]
    top = min(row for row, _ in cells)
    bottom = max(row for row, _ in cells)
    left = min(col for _, col in cells)
    right = max(col for _, col in cells)
    return [line[left:right + 1] for line in grid[top:bottom + 1]]
