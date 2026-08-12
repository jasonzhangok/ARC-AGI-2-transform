def transform(grid):
    out = [row[:] for row in grid]
    h = len(grid)
    w = len(grid[0])
    row_main = [max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in (v for v in row if v)] and count_dict), key=count_dict.get) for row in grid]
    horizontal = all((len(set(row) - {0}) == 1 for row in grid))
    if horizontal:
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 0:
                    color = row_main[r]
                    a = r
                    b = r
                    while a > 0 and row_main[a - 1] == color:
                        a -= 1
                    while b + 1 < h and row_main[b + 1] == color:
                        b += 1
                    for x in range(a, b + 1):
                        out[x][c] = 0
    else:
        col_main = [max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in (grid[r][c] for r in range(h))] and count_dict), key=count_dict.get) for c in range(w)]
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 0:
                    color = col_main[c]
                    a = c
                    b = c
                    while a > 0 and col_main[a - 1] == color:
                        a -= 1
                    while b + 1 < w and col_main[b + 1] == color:
                        b += 1
                    for y in range(a, b + 1):
                        out[r][y] = 0
    output = out
    return output
