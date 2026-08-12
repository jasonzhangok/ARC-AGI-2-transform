from collections import Counter


def transform(grid):
    out=[]
    for br in range(3):
        row=[]
        for bc in range(3):
            values=[grid[r][c] for r in range(br*3,br*3+3) for c in range(bc*3,bc*3+3) if grid[r][c] not in (0,5)]
            row.append(Counter(values).most_common(1)[0][0] if values else 0)
        out.append(row)
    return out
