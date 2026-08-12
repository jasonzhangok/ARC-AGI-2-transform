def transform(grid):
    height, width = (len(grid), len(grid[0]))
    vertical_col = max(((sum((grid[r][_item_1] == 8 for r in range(height))), _index_1, _item_1) for _index_1, _item_1 in enumerate(range(width))))[2]
    seeds = []
    for r, row in enumerate(grid):
        colors = [value for c, value in enumerate(row) if c != vertical_col and value != 7]
        if colors and len(set(colors)) == 1:
            seeds.append((r, colors[0]))
    result = []
    for r in range(height):
        distances = [(abs(r - seed_row), seed_row, color) for seed_row, color in seeds]
        minimum = min((distance for distance, _, _ in distances))
        nearest = [(seed_row, color) for distance, seed_row, color in distances if distance == minimum]
        if len({color for _, color in nearest}) > 1:
            result.append([1] * width)
        else:
            seed_row, color = nearest[0]
            row = [color] * width
            if r == seed_row:
                row = [1] * width
                row[vertical_col] = 8
            else:
                row[vertical_col] = 1
            result.append(row)
    output = result
    return output
