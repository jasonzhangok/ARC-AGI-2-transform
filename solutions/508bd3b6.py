def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    eights = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    horizontal_wall = any((all((v == 2 for v in row)) for row in grid))
    if horizontal_wall:
        wall_row = next((r for r, row in enumerate(grid) if all((v == 2 for v in row))))
        dr = 1 if wall_row > sum((r for r, _ in eights)) / len(eights) else -1
        slope = 1 if len({c - r for r, c in eights}) == 1 else -1
        dc = dr * slope
    else:
        wall_col = next((c for c in range(w) if all((grid[r][c] == 2 for r in range(h)))))
        dc = 1 if wall_col > sum((c for _, c in eights)) / len(eights) else -1
        slope = 1 if len({c - r for r, c in eights}) == 1 else -1
        dr = dc * slope
    r, c = max(((_key_item_1[0] * dr + _key_item_1[1] * dc, -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(eights)))[2]
    reflected = False
    while True:
        nr, nc = (r + dr, c + dc)
        if not (0 <= nr < h and 0 <= nc < w):
            break
        if grid[nr][nc] == 2:
            if reflected:
                break
            if horizontal_wall:
                dr = -dr
            else:
                dc = -dc
            reflected = True
            continue
        if out[nr][nc] == 0:
            out[nr][nc] = 3
        r, c = (nr, nc)
    output = out
    return output
