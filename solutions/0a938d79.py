def transform(grid):
    height, width = len(grid), len(grid[0])
    points = [
        (r, c, value)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value != 0
    ]
    output = [row[:] for row in grid]
    row_distance = abs(points[0][0] - points[1][0])
    column_distance = abs(points[0][1] - points[1][1])

    if row_distance == 0 or (
        column_distance != 0 and column_distance < row_distance
    ):
        points.sort(key=lambda point: point[1])
        start, step = points[0][1], points[1][1] - points[0][1]
        colors = (points[0][2], points[1][2])
        for index, c in enumerate(range(start, width, step)):
            for r in range(height):
                output[r][c] = colors[index % 2]
    else:
        points.sort(key=lambda point: point[0])
        start, step = points[0][0], points[1][0] - points[0][0]
        colors = (points[0][2], points[1][2])
        for index, r in enumerate(range(start, height, step)):
            output[r] = [colors[index % 2]] * width
    return output
