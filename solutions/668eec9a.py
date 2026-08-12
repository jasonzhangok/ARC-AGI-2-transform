def transform(grid):
    colors = [_sort_record_1[2] for _sort_record_1 in sorted(((min((r for r, row in enumerate(grid) if _sort_item_1 in row)), _sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(set((v for row in grid for v in row)) - {7})))]
    colors = [7] * (5 - len(colors)) + colors
    output = [[color] * 3 for color in colors]
    return output
