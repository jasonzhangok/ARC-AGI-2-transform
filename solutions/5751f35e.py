def transform(grid):
    h, w = (len(grid), len(grid[0]))
    layers = {}
    for r in range(h):
        for c in range(w):
            layers.setdefault(min(r, c, h - 1 - r, w - 1 - c), []).append(grid[r][c])
    colors = {d: max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in (x for x in v if x != 0)] and count_dict), key=count_dict.get) if any((x != 0 for x in v)) else 0 for d, v in layers.items()}
    output = [[colors[min(r, c, h - 1 - r, w - 1 - c)] for c in range(w)] for r in range(h)]
    return output
