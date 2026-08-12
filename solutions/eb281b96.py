def transform(grid):
    cycle = grid + grid[-2:0:-1]
    return [cycle[i % len(cycle)][:] for i in range(2 * len(cycle) + 1)]
