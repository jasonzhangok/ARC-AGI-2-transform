def transform(grid):
    output = [[0] * len(grid[0]) for _ in grid]
    for start in range(0, len(grid[0]), 3):
        cells = {
            (row, col)
            for row in range(3)
            for col in range(3)
            if grid[row][start + col] == 5
        }
        if cells == {(1, 1)}:
            color = 4
        elif cells == {(0, 2), (1, 1), (2, 0)}:
            color = 9
        elif cells == {(0, 0), (0, 1), (0, 2)}:
            color = 6
        elif cells == {(2, 0), (2, 1), (2, 2)}:
            color = 1
        else:
            color = 3
        for row in range(3):
            output[row][start:start + 3] = [color] * 3
    return output
