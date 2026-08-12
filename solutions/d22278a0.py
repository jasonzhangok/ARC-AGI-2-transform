def transform(grid):
    height = len(grid)
    width = len(grid[0])
    sources = [
        (row, col, value)
        for row, values in enumerate(grid)
        for col, value in enumerate(values)
        if value != 0
    ]
    output = [[0] * width for _ in range(height)]

    for row in range(height):
        for col in range(width):
            distances = [
                (row - source_row) ** 2 + (col - source_col) ** 2
                for source_row, source_col, _ in sources
            ]
            nearest_distance = min(distances)
            nearest = [
                index
                for index, distance in enumerate(distances)
                if distance == nearest_distance
            ]
            if len(nearest) != 1:
                continue

            source_row, source_col, color = sources[nearest[0]]
            square_radius = max(abs(row - source_row), abs(col - source_col))
            if square_radius % 2 == 0:
                output[row][col] = color

    return output
