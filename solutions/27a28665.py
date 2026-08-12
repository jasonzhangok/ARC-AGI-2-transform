def transform(grid):
    if grid[1][1] == 0:
        color = 1
    elif all(
        grid[row][col] != 0
        for row, col in ((0, 1), (1, 0), (1, 2), (2, 1))
    ):
        color = 6
    elif all(
        grid[row][col] != 0
        for row, col in ((0, 0), (0, 2), (2, 0), (2, 2))
    ):
        color = 2
    else:
        color = 3
    return [[color]]
