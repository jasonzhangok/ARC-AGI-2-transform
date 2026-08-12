def transform(grid):
    factor = len({value for row in grid for value in row})
    return [
        [value for value in row for _ in range(factor)]
        for row in grid
        for _ in range(factor)
    ]
