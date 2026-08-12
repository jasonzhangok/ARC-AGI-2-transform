from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    full_rows = [(r, grid[r][0]) for r in range(height) if len(set(grid[r])) == 1 and grid[r][0] != 0]
    full_cols = [
        (c, grid[0][c])
        for c in range(width)
        if len({grid[r][c] for r in range(height)}) == 1 and grid[0][c] != 0
    ]
    output = [[0] * width for _ in range(height)]
    for row, color in full_rows:
        output[row] = [color] * width
    for col, color in full_cols:
        for row in range(height):
            output[row][col] = color

    for line, color in full_rows:
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color and row != line:
                    target = line - 1 if row < line else line + 1
                    output[target][col] = color
    for line, color in full_cols:
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color and col != line:
                    target = line - 1 if col < line else line + 1
                    output[row][target] = color
    return output
