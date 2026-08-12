def transform(grid):
    twos = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2]
    r0 = min(r for r, _ in twos)
    r1 = max(r for r, _ in twos)
    c0 = min(c for _, c in twos)
    c1 = max(c for _, c in twos)

    cells = [(r, c) for r in range(r0 + 1, r1) for c in range(c0 + 1, c1)
             if grid[r][c] not in (0, 2)]
    sr0 = min(r for r, _ in cells)
    sr1 = max(r for r, _ in cells)
    sc0 = min(c for _, c in cells)
    sc1 = max(c for _, c in cells)
    seed = [row[sc0:sc1 + 1] for row in grid[sr0:sr1 + 1]]
    sy = (r1 - r0 - 1) // len(seed)
    sx = (c1 - c0 - 1) // len(seed[0])
    out = [[2] * (c1 - c0 + 1)]
    for r in range(r0 + 1, r1):
        row = [2]
        for c in range(c0 + 1, c1):
            row.append(seed[(r - r0 - 1) // sy][(c - c0 - 1) // sx])
        row.append(2)
        out.append(row)
    out.append([2] * (c1 - c0 + 1))
    output = out
    return output
