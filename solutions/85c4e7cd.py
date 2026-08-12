def transform(grid):
    h, w = len(grid), len(grid[0])
    layers = min(h, w) // 2
    colors = [grid[k][k] for k in range(layers)]
    replacement = dict(zip(colors, reversed(colors)))
    output = [[replacement[value] for value in row] for row in grid]
    return output
