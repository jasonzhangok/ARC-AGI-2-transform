def transform(grid):
    h, w = (len(grid), len(grid[0]))
    colors = {v for row in grid for v in row if v != 0}
    info = {}
    for color in colors:
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        box = (min((r for r, _ in cells)), max((r for r, _ in cells)), min((c for _, c in cells)), max((c for _, c in cells)))
        area = (box[1] - box[0] + 1) * (box[3] - box[2] + 1)
        info[color] = (len(cells) / area, box)
    frame = min(((info[_key_item_1][0], _key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(colors)))[2]
    marker = next((color for color in colors if color != frame))
    r0, r1, c0, c1 = info[frame][1]
    mr0, mr1, mc0, mc1 = info[marker][1]
    out = [row[:] for row in grid]
    rays = ((mr0, mc0, -1, -1), (mr0, mc1, -1, 1), (mr1, mc0, 1, -1), (mr1, mc1, 1, 1))
    for r, c, dr, dc in rays:
        crossed = False
        while True:
            r, c = (r + dr, c + dc)
            if not (0 <= r < h and 0 <= c < w):
                break
            if grid[r][c] == frame:
                crossed = True
            if crossed and (not (r0 <= r <= r1 and c0 <= c <= c1)):
                out[r][c] = marker
    output = out
    return output
