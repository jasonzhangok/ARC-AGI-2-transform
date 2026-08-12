def transform(grid):
    period = next(
        size
        for size in range(1, len(grid) + 1)
        if all(grid[r] == grid[r % size] for r in range(len(grid)))
    )
    return [
        [2 if value == 1 else value for value in grid[r % period]]
        for r in range(9)
    ]
