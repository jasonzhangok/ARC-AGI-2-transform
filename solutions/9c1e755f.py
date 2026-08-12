def transform(grid):
    out = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    horizontal = []
    for r in range(h):
        c = 0
        while c < w:
            if grid[r][c] != 5:
                c += 1
                continue
            left = c
            while c < w and grid[r][c] == 5:
                c += 1
            if c - left >= 2:
                horizontal.append((r, left, c - 1))
    for line_r, left, right in horizontal:
        anchor = max(((sum((grid[r][_key_item_1] not in (0, 5) for r in range(h))), -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(range(left, right + 1))))[2]
        for r in range(h):
            color = grid[r][anchor]
            if color not in (0, 5):
                for c in range(left, right + 1):
                    out[r][c] = color
    vertical = []
    for c in range(w):
        r = 0
        while r < h:
            if grid[r][c] != 5:
                r += 1
                continue
            top = r
            while r < h and grid[r][c] == 5:
                r += 1
            if r - top >= 2:
                vertical.append((c, top, r - 1))
    for line_c, top, bottom in vertical:
        candidate_rows = []
        for r in range(top, bottom + 1):
            adjacent = []
            if line_c > 0:
                adjacent.append(grid[r][line_c - 1])
            if line_c + 1 < w:
                adjacent.append(grid[r][line_c + 1])
            if any((value not in (0, 5) for value in adjacent)):
                candidate_rows.append(r)
        if not candidate_rows:
            continue
        seed_top = min(candidate_rows)
        seed_bottom = max(candidate_rows)
        period = seed_bottom - seed_top + 1
        for r in range(top, bottom + 1):
            source_r = seed_top + (r - seed_top) % period
            for c in range(w):
                color = grid[source_r][c]
                if color not in (0, 5):
                    out[r][c] = color
    output = out
    return output
