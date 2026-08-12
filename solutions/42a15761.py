def transform(grid):
    height, width = (len(grid), len(grid[0]))
    block_count = (width + 1) // 4
    blocks = [[row[4 * index:4 * index + 3] for row in grid] for index in range(block_count)]
    blocks = [_sort_record_1[2] for _sort_record_1 in sorted(((sum((row[1] == 0 for row in _sort_item_1)), _sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(blocks)))]
    output = []
    for row in range(height):
        combined = []
        for index, block in enumerate(blocks):
            if index:
                combined.append(0)
            combined.extend(block[row])
        output.append(combined)
    return output
