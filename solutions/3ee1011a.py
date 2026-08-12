def transform(grid):
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    layers = [_record_1[2] for _record_1 in sorted(((_item_1[1], -_index_1, _item_1) for _index_1, _item_1 in enumerate(counts.items())), reverse=True)]
    size = layers[0][1]
    result = [[0 for _ in range(size)] for _ in range(size)]
    for inset, (color, _) in enumerate(layers):
        low, high = (inset, size - 1 - inset)
        for position in range(low, high + 1):
            result[low][position] = color
            result[high][position] = color
            result[position][low] = color
            result[position][high] = color
    output = result
    return output
