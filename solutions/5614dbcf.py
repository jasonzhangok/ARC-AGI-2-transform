def transform(grid):
    out = []
    for br in range(3):
        row = []
        for bc in range(3):
            values = [grid[r][c] for r in range(br * 3, br * 3 + 3) for c in range(bc * 3, bc * 3 + 3) if grid[r][c] not in (0, 5)]
            row.append(max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in values] and count_dict), key=count_dict.get) if values else 0)
        out.append(row)
    output = out
    return output
