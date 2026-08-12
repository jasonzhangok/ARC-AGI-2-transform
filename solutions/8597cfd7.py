def transform(grid):
    divider = next((r for r, row in enumerate(grid) if row.count(5) == len(row)))
    colors = sorted(set((v for row in grid for v in row)) - {0, 5})
    score = {color: abs(sum((grid[r][c] == color for r in range(divider) for c in range(len(grid[0])))) - sum((grid[r][c] == color for r in range(divider + 1, len(grid)) for c in range(len(grid[0]))))) for color in colors}
    color = max((((score[_key_item_1], -_key_item_1), -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(colors)))[2]
    output = [[color, color], [color, color]]
    return output
