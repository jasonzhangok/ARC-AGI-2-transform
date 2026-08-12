def transform(grid):
    h, w = (len(grid), len(grid[0]))
    twos = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    r0, r1 = (min((r for r, _ in twos)), max((r for r, _ in twos)))
    c0, c1 = (min((c for _, c in twos)), max((c for _, c in twos)))
    cr, cc = ((r0 + r1) // 2, (c0 + c1) // 2)
    markers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3 and (r, c) != (cr, cc)]
    if all((r == cr for r, _ in markers)):
        left = [p for p in markers if p[1] < cc]
        right = [p for p in markers if p[1] > cc]
        target = min(((_key_item_1[1], _key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(right)))[2] if len(right) >= len(left) else max(((_key_item_2[1], -_key_index_2, _key_item_2) for _key_index_2, _key_item_2 in enumerate(left)))[2]
    else:
        above = [p for p in markers if p[0] < cr]
        below = [p for p in markers if p[0] > cr]
        target = min(((_key_item_3[0], _key_index_3, _key_item_3) for _key_index_3, _key_item_3 in enumerate(below)))[2] if len(below) >= len(above) else max(((_key_item_4[0], -_key_index_4, _key_item_4) for _key_index_4, _key_item_4 in enumerate(above)))[2]
    dr, dc = (target[0] - cr, target[1] - cc)
    out = [[0 if v == 2 else v for v in row] for row in grid]
    for r, c in twos:
        out[r + dr][c + dc] = 2
    out[target[0]][target[1]] = 3
    output = out
    return output
