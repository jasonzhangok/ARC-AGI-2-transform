def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    separator = next(r for r, row in enumerate(grid) if all(value == 5 for value in row))
    for r in range(h):
        if r == separator:
            continue
        for c, color in enumerate(grid[r]):
            if color not in (1, 2):
                continue
            if r < separator:
                rows = range(r, separator) if color == 2 else range(0, r + 1)
            else:
                rows = range(separator + 1, r + 1) if color == 2 else range(r, h)
            for x in rows:
                output[x][c] = color
    return output
