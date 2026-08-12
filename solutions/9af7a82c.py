def transform(grid):
    counts = {}
    for cell_value in (value for row in grid for value in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    colors = [_record_1[2] for _record_1 in sorted((((-counts[_item_1], _item_1), _index_1, _item_1) for _index_1, _item_1 in enumerate(counts)))]
    height = counts[colors[0]]
    output = [[color if r < counts[color] else 0 for color in colors] for r in range(height)]
    return output
