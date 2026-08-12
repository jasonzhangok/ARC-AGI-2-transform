def transform(grid):
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    output = [[value] for value in [_sort_record_1[2] for _sort_record_1 in sorted(((counts[_sort_item_1], -_sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(counts)), reverse=True)]]
    return output
