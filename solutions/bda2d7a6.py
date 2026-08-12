def transform(grid):
    colors = []
    for i in range(min(len(grid), len(grid[0]))):
        value = grid[i][i]
        if value not in colors:
            colors.append(value)
    replacement = {value: colors[i - 1] for i, value in enumerate(colors)}
    output = [[replacement.get(value, value) for value in row] for row in grid]
    return output
