def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    best = None
    for top in range(h):
        all_zero = [True] * w
        for bottom in range(top, h):
            all_zero = [all_zero[c] and grid[bottom][c] == 0 for c in range(w)]
            c = 0
            while c < w:
                if not all_zero[c]:
                    c += 1
                    continue
                left = c
                while c < w and all_zero[c]:
                    c += 1
                width = c - left
                height = bottom - top + 1
                if height >= width:
                    candidate = (width * height, top, bottom, left, c - 1)
                    if best is None or candidate[0] > best[0]:
                        best = candidate

    _, raw_top, raw_bottom, raw_left, raw_right = best
    top = raw_top + (raw_top > 0)
    bottom = raw_bottom - (raw_bottom < h - 1)
    left = raw_left + (raw_left > 0)
    right = raw_right - (raw_right < w - 1)
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            out[r][c] = 3

    for side_left, side_right in ((0, left - 1), (right + 1, w - 1)):
        if side_left > side_right:
            continue
        blank_rows = [all(grid[r][c] == 0
                          for c in range(side_left, side_right + 1))
                      for r in range(h)]
        r = 0
        while r < h:
            if not blank_rows[r]:
                r += 1
                continue
            run_top = r
            while r < h and blank_rows[r]:
                r += 1
            run_bottom = r - 1
            if run_bottom - run_top + 1 < 3:
                continue
            core_top = run_top + (run_top > 0)
            core_bottom = run_bottom - (run_bottom < h - 1)
            for nr in range(max(core_top, top), min(core_bottom, bottom) + 1):
                for c in range(side_left, side_right + 1):
                    out[nr][c] = 3
    return out
