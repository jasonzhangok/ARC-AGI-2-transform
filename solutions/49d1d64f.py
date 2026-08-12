def transform(grid):
    w = len(grid[0])
    out = [[0] + grid[0][:] + [0]]
    out.extend([[row[0]] + row[:] + [row[-1]] for row in grid])
    out.append([0] + grid[-1][:] + [0])
    return out
