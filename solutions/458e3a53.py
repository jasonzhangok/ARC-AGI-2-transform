def transform(grid):
    h, w = len(grid), len(grid[0])
    separator_rows = [r for r, row in enumerate(grid) if len(set(row)) == 1]
    separator = grid[separator_rows[0]][0]
    separator_cols = [
        c for c in range(w) if all(grid[r][c] == separator for r in range(h))
    ]

    row_bounds = [-1] + separator_rows + [h]
    rows = [(row_bounds[i] + 1, row_bounds[i + 1]) for i in range(len(row_bounds) - 1)
            if row_bounds[i] + 1 < row_bounds[i + 1]]
    col_bounds = [-1] + separator_cols + [w]
    cols = [(col_bounds[i] + 1, col_bounds[i + 1]) for i in range(len(col_bounds) - 1)
            if col_bounds[i] + 1 < col_bounds[i + 1]]
    uniform = {}
    for i, (r0, r1) in enumerate(rows):
        for j, (c0, c1) in enumerate(cols):
            values = {grid[r][c] for r in range(r0, r1) for c in range(c0, c1)}
            if len(values) == 1:
                uniform[i, j] = values.pop()
    r_ids = [i for i, _ in uniform]
    c_ids = [j for _, j in uniform]
    r0, r1 = min(r_ids), max(r_ids)
    c0, c1 = min(c_ids), max(c_ids)
    output = [[uniform[i, j] for j in range(c0, c1 + 1)] for i in range(r0, r1 + 1)]
    return output
