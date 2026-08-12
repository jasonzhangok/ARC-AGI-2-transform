def transform(grid):
    cells = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 8]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    r0 -= 3 - (r1 - r0 + 1)
    c0 -= 3 - (c1 - c0 + 1)
    tile = [row[c0:c0 + 3] for row in grid[r0:r0 + 3]]
    copies = sum(v == 4 for row in grid for v in row)
    return [row * copies for row in tile]
