def transform(grid):
    result = [row[:] for row in grid]
    for r, row in enumerate(grid):
        points = [(c, value) for c, value in enumerate(row) if value != 0]
        if len(points) == 2:
            (left, left_color), (right, right_color) = points
            middle = (left + right) // 2
            for c in range(left, middle):
                result[r][c] = left_color
            result[r][middle] = 5
            for c in range(middle + 1, right + 1):
                result[r][c] = right_color
    return result
