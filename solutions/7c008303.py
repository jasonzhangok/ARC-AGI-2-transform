def transform(grid):
    sep_rows = [r for r, row in enumerate(grid) if row.count(8) == len(row)]
    sep_cols = [c for c in range(len(grid[0])) if all(row[c] == 8 for row in grid)]
    sr, sc = sep_rows[0], sep_cols[0]
    regions = [
        (0, sr, 0, sc), (0, sr, sc + 1, len(grid[0])),
        (sr + 1, len(grid), 0, sc),
        (sr + 1, len(grid), sc + 1, len(grid[0])),
    ]
    pieces = [[row[c0:c1] for row in grid[r0:r1]] for r0, r1, c0, c1 in regions]
    key = next(p for p in pieces if len(p) == 2 and len(p[0]) == 2)
    target = next(p for p in pieces if len(p) == 6 and len(p[0]) == 6)
    return [[key[r // 3][c // 3] if target[r][c] == 3 else 0
             for c in range(6)] for r in range(6)]
