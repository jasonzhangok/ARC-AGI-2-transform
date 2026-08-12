def transform(grid):
    cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row)
             if value != 0]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    crop = [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
    out = []
    for row in crop:
        expanded = [value for value in row for _ in range(2)]
        out.extend((expanded[:], expanded[:]))
    output = out
    return output
