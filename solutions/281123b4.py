def transform(grid):
    starts = (0, 5, 10, 15)
    priority = {0: 0, 5: 1, 8: 2, 4: 3, 9: 4}
    result = []
    for row in grid:
        output_row = []
        for c in range(4):
            candidates = [row[start + c] for start in starts]
            output_row.append(max(((priority[_key_item_1], -_key_index_1, _key_item_1) for _key_index_1, _key_item_1 in enumerate(candidates)))[2])
        result.append(output_row)
    output = result
    return output
