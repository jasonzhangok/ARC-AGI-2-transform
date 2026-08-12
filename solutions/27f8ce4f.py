def transform(grid):
    height, width = (len(grid), len(grid[0]))
    dominant = {}
    for cell_value in (value for row in grid for value in row):
        dominant[cell_value] = dominant.get(cell_value, 0) + 1
    dominant = max(dominant, key=dominant.get)
    result = [[0] * (width * height) for _ in range(height * height)]
    for macro_r in range(height):
        for macro_c in range(width):
            if grid[macro_r][macro_c] == dominant:
                for r in range(height):
                    for c in range(width):
                        result[macro_r * height + r][macro_c * width + c] = grid[r][c]
    output = result
    return output
