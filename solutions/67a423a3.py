def transform(grid):
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    vr = max(((sum((grid[r][_key_item_1] != 0 for r in range(h))), -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(range(w))))[2]
    hr = max(((sum((v != 0 for v in grid[_key_item_2])), -_key_index_2, _key_item_2) for _key_index_2, _key_item_2 in enumerate(range(h))))[2]
    center = grid[hr][vr]
    for r in range(max(0, hr - 1), min(h, hr + 2)):
        for c in range(max(0, vr - 1), min(w, vr + 2)):
            out[r][c] = 4
    out[hr][vr] = center
    output = out
    return output
