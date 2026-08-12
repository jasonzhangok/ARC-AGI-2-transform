def transform(grid):
    points = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0}
    components = []
    while points:
        start = points.pop()
        stack = [start]
        component = {start}
        while stack:
            row, col = stack.pop()
            neighbors = {(r, c) for r, c in points if abs(r - row) <= 2 and abs(c - col) <= 2}
            points -= neighbors
            component |= neighbors
            stack.extend(neighbors)
        components.append(component)
    components = [_sort_record_1[2] for _sort_record_1 in sorted((((min((r for r, _ in _sort_item_1)), min((c for _, c in _sort_item_1))), _sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(components)))]
    top_two = [_sort_record_2[2] for _sort_record_2 in sorted(((min((c for _, c in _sort_item_2)), _sort_index_2, _sort_item_2) for _sort_index_2, _sort_item_2 in enumerate(components[:2])))]
    bottom_two = [_sort_record_3[2] for _sort_record_3 in sorted(((min((c for _, c in _sort_item_3)), _sort_index_3, _sort_item_3) for _sort_index_3, _sort_item_3 in enumerate(components[2:])))]
    ordered = top_two + bottom_two
    output = [[0] * 7 for _ in range(7)]
    for index, component in enumerate(ordered):
        top = min((r for r, _ in component))
        left = min((c for _, c in component))
        target_row = 0 if index < 2 else 4
        target_col = 0 if index % 2 == 0 else 4
        for row, col in component:
            output[target_row + row - top][target_col + col - left] = grid[row][col]
    return output
