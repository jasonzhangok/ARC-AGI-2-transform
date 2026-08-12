def transform(grid):
    height, width = (len(grid), len(grid[0]))
    seeds = sorted(((r, value) for r, row in enumerate(grid) for value in row if value != 0))
    output = [[0] * width for _ in range(height)]
    for r in range(height):
        seed_row, color = min((((abs(_key_item_1[0] - r), _key_item_1[0]), _key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(seeds)))[2]
        output[r][0] = color
        output[r][-1] = color
    for r, color in seeds:
        output[r] = [color] * width
    output[0] = [seeds[0][1]] * width
    output[-1] = [seeds[-1][1]] * width
    return output
