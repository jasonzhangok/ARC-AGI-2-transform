def transform(grid):
    height, width = len(grid), len(grid[0])
    border = [(0, c) for c in range(width)]
    border += [(r, width - 1) for r in range(1, height)]
    border += [(height - 1, c) for c in range(width - 2, -1, -1)]
    border += [(r, 0) for r in range(height - 2, 0, -1)]

    marker = next(value for row in grid for value in row if value != 8)
    marked = {index for index, (r, c) in enumerate(border) if grid[r][c] == marker}
    period_length = len(marked)
    start = next(index for index in marked if (index - 1) % len(border) not in marked)

    result = [row[:] for row in grid]
    for index, (r, c) in enumerate(border):
        if (index - start) % (2 * period_length) < period_length:
            result[r][c] = marker
    return result
