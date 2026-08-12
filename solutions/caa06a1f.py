def transform(grid):
    first = grid[0][0]
    second = grid[0][1]
    return [
        [second if (row + col) % 2 == 0 else first
         for col in range(len(grid[0]))]
        for row in range(len(grid))
    ]
