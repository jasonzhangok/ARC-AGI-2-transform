def transform(grid):
    size = len(grid)
    output = [[0] * (size * size) for _ in range(size * size)]
    uniform_row = next((r for r in range(size) if len(set(grid[r])) == 1), None)
    if uniform_row is not None:
        top = uniform_row * size
        for repeat in range(size):
            for row in range(size):
                for col in range(size):
                    output[top + row][repeat * size + col] = grid[row][col]
    else:
        uniform_col = next(c for c in range(size) if len({grid[r][c] for r in range(size)}) == 1)
        left = uniform_col * size
        for repeat in range(size):
            for row in range(size):
                for col in range(size):
                    output[repeat * size + row][left + col] = grid[row][col]
    return output
