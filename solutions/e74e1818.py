def transform(grid):
    output = [row[:] for row in grid]
    for color in {value for row in grid for value in row if value != 0}:
        cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color]
        r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
        for r, c in cells:
            output[r][c] = 0
        for r, c in cells:
            output[r0 + r1 - r][c] = color
    return output
