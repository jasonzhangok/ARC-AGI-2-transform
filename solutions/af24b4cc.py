def transform(grid):
    groups = []
    rows = []
    for row in grid + [[0] * len(grid[0])]:
        if any(row):
            rows.append(row)
        elif rows:
            groups.append(rows)
            rows = []
    encoded = []
    for block in groups:
        colors = []
        for c in range(1, len(block[0]) - 1, 3):
            colors.append(max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in (block[r][x] for r in range(len(block)) for x in range(c, min(c + 2, len(block[0]))) if block[r][x])] and count_dict), key=count_dict.get))
        encoded.append([0] + colors + [0])
    width = len(encoded[0])
    output = [[0] * width] + encoded + [[0] * width]
    return output
