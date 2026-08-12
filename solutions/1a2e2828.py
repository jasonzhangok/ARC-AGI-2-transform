from collections import Counter


def transform(grid):
    colors = {value for row in grid for value in row if value != 0}
    for color in colors:
        if any(all(value == color for value in row) for row in grid):
            return [[color]]
        for col in range(len(grid[0])):
            if all(grid[row][col] == color for row in range(len(grid))):
                return [[color]]
    raise ValueError("no uninterrupted full-length colored line")
