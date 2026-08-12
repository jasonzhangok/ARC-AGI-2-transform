def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [[0] * width for _ in range(height)]
    for top in range(1, height, 4):
        for left in range(1, width, 4):
            for row in range(top, min(top + 3, height)):
                for col in range(left, min(left + 3, width)):
                    if grid[row][col] == 0:
                        output[row][col] = 2
    return output
