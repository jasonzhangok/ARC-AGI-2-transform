

def transform(grid):
    n = len(grid)
    dominant = {}
    for cell_value in (value for row in grid for value in row):
        dominant[cell_value] = dominant.get(cell_value, 0) + 1
    dominant = max(dominant, key=dominant.get)
    output = [[0] * (n * n) for _ in range(n * n)]
    for block_r in range(n):
        for block_c in range(n):
            if grid[block_r][block_c] == dominant:
                for r in range(n):
                    for c in range(n):
                        output[block_r * n + r][block_c * n + c] = grid[r][c]
    return output
