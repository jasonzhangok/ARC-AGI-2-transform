def transform(grid):
    cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    r0, r1 = (min((r for r, _ in cells)), max((r for r, _ in cells)))
    c0, c1 = (min((c for _, c in cells)), max((c for _, c in cells)))
    colors = list((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in (grid[r][c] for r, c in cells)] and count_dict))
    a, b = colors
    output = [[b if grid[r][c] == a else a if grid[r][c] == b else 0 for c in range(c0, c1 + 1)] for r in range(r0, r1 + 1)]
    return output
