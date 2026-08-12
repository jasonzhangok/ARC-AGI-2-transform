def transform(grid):
    mirrored_rows = [list(reversed(row)) + row[:] for row in grid]
    flipped = [row[:] for row in reversed(mirrored_rows)]
    return flipped + [row[:] for row in mirrored_rows] + [row[:] for row in flipped]
