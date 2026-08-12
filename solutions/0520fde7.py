def transform(grid):
    height, width = len(grid), len(grid[0])
    separator = next(
        c for c in range(width) if all(grid[r][c] == 5 for r in range(height))
    )
    result_width = min(separator, width - separator - 1)
    return [
        [
            2
            if grid[r][c] != 0 and grid[r][separator + 1 + c] != 0
            else 0
            for c in range(result_width)
        ]
        for r in range(height)
    ]
