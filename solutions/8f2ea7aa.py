

def transform(grid):
    h, w = len(grid), len(grid[0])
    color = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        color[cell_value] = color.get(cell_value, 0) + 1
    color = max(color, key=color.get)
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    motif = [row[c0:c1 + 1] for row in grid[r0:r1 + 1]]
    mh, mw = len(motif), len(motif[0])
    output = [[0] * w for _ in range(h)]
    for br in range(mh):
        for bc in range(mw):
            if motif[br][bc] != 0:
                for r in range(mh):
                    for c in range(mw):
                        if motif[r][c] != 0:
                            output[br * mh + r][bc * mw + c] = color
    return output
