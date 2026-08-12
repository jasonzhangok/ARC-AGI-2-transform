def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    gray = [
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] == 5
    ]
    top, bottom = min(r for r, _ in gray), max(r for r, _ in gray)
    left, right = min(c for _, c in gray), max(c for _, c in gray)

    empty_rows = [
        r for r in range(top, bottom + 1)
        if all(grid[r][c] != 5 for c in range(left, right + 1))
    ]
    empty_columns = [
        c for c in range(left, right + 1)
        if all(grid[r][c] != 5 for r in range(top, bottom + 1))
    ]
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if output[r][c] == 0:
                output[r][c] = 2
    for r in empty_rows:
        for c in list(range(0, left)) + list(range(right + 1, width)):
            output[r][c] = 1
    for c in empty_columns:
        for r in list(range(0, top)) + list(range(bottom + 1, height)):
            output[r][c] = 1
    return output
