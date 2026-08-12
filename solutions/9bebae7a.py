def transform(grid):
    out = [row[:] for row in grid]
    six = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 6]
    four = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 4]
    for r, c in six:
        out[r][c] = 0
    max_h = max(sum(grid[r][c] == 6 for c in range(len(grid[0]))) for r in range(len(grid)))
    max_v = max(sum(grid[r][c] == 6 for r in range(len(grid))) for c in range(len(grid[0])))
    if max_h > max_v:
        bar_row = max(range(len(grid)), key=lambda r: sum(v == 6 for v in grid[r]))
        bar_cols = [c for c, v in enumerate(grid[bar_row]) if v == 6]
        stem_col = max(range(len(grid[0])), key=lambda c: sum(grid[r][c] == 6 for r in range(len(grid))))
        if stem_col >= (min(bar_cols) + max(bar_cols)) / 2:
            edge = max(r for r, _ in four)
            for r, c in four:
                nr = 2 * edge + 1 - r
                if 0 <= nr < len(out):
                    out[nr][c] = 4
        else:
            edge = min(r for r, _ in four)
            for r, c in four:
                nr = 2 * edge - 1 - r
                if 0 <= nr < len(out):
                    out[nr][c] = 4
    else:
        edge = max(c for _, c in four)
        for r, c in four:
            nc = 2 * edge + 1 - c
            if 0 <= nc < len(out[0]):
                out[r][nc] = 4
    return out
