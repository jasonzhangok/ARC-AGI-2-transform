def transform(grid):
    h = len(grid)
    w = len(grid[0])
    missing = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0:
                missing.append((r, c))
    if not missing:
        return [row[:] for row in grid]

    pattern = None
    chosen_row_period = 0
    chosen_col_period = 0
    for area in range(1, h * w + 1):
        if pattern is not None:
            break
        for row_period in range(1, h + 1):
            if area % row_period != 0:
                continue
            col_period = area // row_period
            if col_period < 1 or col_period > w:
                continue
            known = {}
            valid = True
            for r in range(h):
                if not valid:
                    break
                for c in range(w):
                    if grid[r][c] == 0:
                        continue
                    key = (r % row_period, c % col_period)
                    if key in known and known[key] != grid[r][c]:
                        valid = False
                        break
                    known[key] = grid[r][c]
            if valid:
                for r, c in missing:
                    if (r % row_period, c % col_period) not in known:
                        valid = False
                        break
            if valid:
                pattern = known
                chosen_row_period = row_period
                chosen_col_period = col_period
                break

    top = missing[0][0]
    bottom = missing[0][0]
    left = missing[0][1]
    right = missing[0][1]
    for r, c in missing:
        if r < top:
            top = r
        if r > bottom:
            bottom = r
        if c < left:
            left = c
        if c > right:
            right = c
    output = []
    for r in range(top, bottom + 1):
        row = []
        for c in range(left, right + 1):
            if pattern is None:
                row.append(grid[r][c])
            else:
                row.append(pattern[(r % chosen_row_period, c % chosen_col_period)])
        output.append(row)
    return output
