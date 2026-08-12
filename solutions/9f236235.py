from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [r for r in range(h) if len(set(grid[r])) == 1 and grid[r][0] != 0]
    sep_cols = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1 and grid[0][c] != 0]
    row_parts, start = [], 0
    for r in sep_rows + [h]:
        if start < r: row_parts.append((start, r))
        start = r + 1
    col_parts, start = [], 0
    for c in sep_cols + [w]:
        if start < c: col_parts.append((start, c))
        start = c + 1
    return [[Counter(grid[r][c] for r in range(a, b) for c in range(x, y)).most_common(1)[0][0]
             for x, y in reversed(col_parts)] for a, b in row_parts]
