def transform(grid):
    height = len(grid)
    width = len(grid[0])
    endpoints = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 8:
                endpoints.append((row, column))
    if len(endpoints) != 2:
        output = [row[:] for row in grid]
    else:
        first = endpoints[0]
        second = endpoints[1]
        endpoint_distance = max(abs(first[0] - second[0]), abs(first[1] - second[1]))
        top = min(first[0], second[0])
        bottom = max(first[0], second[0])
        left = min(first[1], second[1])
        right = max(first[1], second[1])
        path_union = set()
        for row in range(top, bottom + 1):
            for column in range(left, right + 1):
                first_distance = max(abs(row - first[0]), abs(column - first[1]))
                second_distance = max(abs(row - second[0]), abs(column - second[1]))
                if first_distance + second_distance == endpoint_distance:
                    path_union.add((row, column))
        output = [row[:] for row in grid]
        for row, column in path_union:
            if grid[row][column] == 8:
                continue
            on_boundary = False
            for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (row + row_step, column + column_step) not in path_union:
                    on_boundary = True
                    break
            if on_boundary:
                output[row][column] = 3
        output = output
    return output
