def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set(value for row in grid for value in row) - {0}
    columns = []
    for color in colors:
        rows = {
            row
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        columns.append((max(rows) - min(rows) + 1, color))
    columns.sort(reverse=True)

    output_height = max(column_height for column_height, _ in columns)
    output = [[0] * len(columns) for _ in range(output_height)]
    for col, (column_height, color) in enumerate(columns):
        for row in range(column_height):
            output[row][col] = color
    return output
