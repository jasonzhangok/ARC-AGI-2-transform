def transform(grid):
    h, w = (len(grid), len(grid[0]))
    cutsr = [-1] + [r for r, row in enumerate(grid) if all((v == 0 for v in row))] + [h]
    cutsc = [-1] + [c for c in range(w) if all((grid[r][c] == 0 for r in range(h)))] + [w]
    rs = [(a + 1, b) for a, b in zip(cutsr, cutsr[1:]) if b > a + 1]
    cs = [(a + 1, b) for a, b in zip(cutsc, cutsc[1:]) if b > a + 1]
    output = [[max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in (grid[r][c] for r in range(r0, r1) for c in range(c0, c1) if grid[r][c])] and count_dict), key=count_dict.get) for c0, c1 in cs] for r0, r1 in rs]
    return output
