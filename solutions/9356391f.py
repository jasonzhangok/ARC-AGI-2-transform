from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    separator = next(r for r, row in enumerate(grid) if row and all(value == 5 for value in row))
    center = next((r, c) for r in range(separator + 1, h) for c in range(w) if grid[r][c] != 0)
    last = max(c for c, value in enumerate(grid[0]) if value != 0)
    rings = grid[0][:last + 1]
    output = [row[:] for row in grid]
    cr, cc = center
    for r in range(separator + 1, h):
        for c in range(w):
            distance = max(abs(r - cr), abs(c - cc))
            if distance < len(rings):
                output[r][c] = rings[distance]
    if 0 in rings:
        first_gap = rings.index(0)
        for c in range(first_gap + 1, len(rings)):
            output[0][c] = 5
    return output
