def transform(grid):
    color = {}
    for cell_value in (v for row in grid for v in row):
        color[cell_value] = color.get(cell_value, 0) + 1
    color = max(color, key=color.get)
    output = [[color] * len(grid[0]) for _ in grid]
    return output
