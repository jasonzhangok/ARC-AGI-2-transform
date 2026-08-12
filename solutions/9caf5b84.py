def transform(grid):
    counts = {}
    for cell_value in (v for row in grid for v in row):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    keep = {color for color, _ in [_record_1[2] for _record_1 in sorted(((-_item_1[1], _index_1, _item_1) for _index_1, _item_1 in enumerate(counts.items())))][:2]}
    output = [[v if v in keep else 7 for v in row] for row in grid]
    return output
