def transform(grid):
    height, width = (len(grid), len(grid[0]))
    points = [(r, c, value) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    output = [row[:] for row in grid]
    row_distance = abs(points[0][0] - points[1][0])
    column_distance = abs(points[0][1] - points[1][1])
    if row_distance == 0 or (column_distance != 0 and column_distance < row_distance):
        points = [_sort_record_1[2] for _sort_record_1 in sorted(((_sort_item_1[1], _sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(points)))]
        start, step = (points[0][1], points[1][1] - points[0][1])
        colors = (points[0][2], points[1][2])
        for index, c in enumerate(range(start, width, step)):
            for r in range(height):
                output[r][c] = colors[index % 2]
    else:
        points = [_sort_record_2[2] for _sort_record_2 in sorted(((_sort_item_2[0], _sort_index_2, _sort_item_2) for _sort_index_2, _sort_item_2 in enumerate(points)))]
        start, step = (points[0][0], points[1][0] - points[0][0])
        colors = (points[0][2], points[1][2])
        for index, r in enumerate(range(start, height, step)):
            output[r] = [colors[index % 2]] * width
    return output
