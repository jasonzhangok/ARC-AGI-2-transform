def transform(grid):
    bg = {}
    for cell_value in (v for row in grid for v in row):
        bg[cell_value] = bg.get(cell_value, 0) + 1
    bg = max(bg, key=bg.get)
    top = grid[0][:]
    middle = grid[1][:]
    bottom = [6 if v != bg else bg for v in top]
    output = [top, middle, bottom]
    return output
