def transform(grid):
    height, width = (len(grid), len(grid[0]))
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    columns = []
    for c in range(width):
        cells = [(r, grid[r][c]) for r in range(height) if grid[r][c] != background]
        if cells:
            columns.append((c, len(cells), cells[0][1]))
    colors = [color for _, _, color in columns]
    rotated_colors = colors[-1:] + colors[:-1]
    lengths = [length for _, length, _ in columns]
    shifted_lengths = lengths[1:] + lengths[:1]
    result = [[background] * width for _ in range(height)]
    for (column, _, _), length, color in zip(columns, shifted_lengths, rotated_colors):
        for r in range(height - length, height):
            result[r][column] = color
    output = result
    return output
