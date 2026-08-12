def transform(grid):
    h, w = len(grid), len(grid[0])
    split = h // 2
    output = [row[:] + [9] for row in grid[:split]]
    output.append([9] * (w + 1))
    output.extend([[9] + row[:] for row in grid[split:]])
    return output
