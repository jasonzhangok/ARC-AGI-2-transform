def transform(grid):
    rows = []
    for row in grid:
        if 1 not in row or 8 not in row:
            continue
        a, b = row.index(1), row.index(8)
        lo, hi = sorted((a, b))
        rows.append(row[lo + 1:hi])
    return rows
