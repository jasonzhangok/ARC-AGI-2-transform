from collections import Counter


def transform(grid):
    line = Counter(v for row in grid for v in row if v).most_common(1)[0][0]
    cells = [(r, c, v) for r, row in enumerate(grid) for c, v in enumerate(row)
             if v not in (0, line)]
    rows = sorted({r for r, _, _ in cells})
    cols = sorted({c for _, c, _ in cells})
    logical = [[grid[r][c] if grid[r][c] != line else 0 for c in cols]
               for r in rows]
    out = [[0] * (len(cols) - 1) for _ in range(len(rows) - 1)]
    for r in range(len(out)):
        for c in range(len(out[0])):
            block = {logical[r][c], logical[r + 1][c],
                     logical[r][c + 1], logical[r + 1][c + 1]}
            if len(block) == 1 and 0 not in block:
                out[r][c] = block.pop()
    return out
