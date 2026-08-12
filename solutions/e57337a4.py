def transform(grid):
    color = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        color[cell_value] = color.get(cell_value, 0) + 1
    color = max(color, key=color.get)
    output = [[0 if any((grid[r][c] == 0 for r in range(br * 5, br * 5 + 5) for c in range(bc * 5, bc * 5 + 5))) else color for bc in range(3)] for br in range(3)]
    return output
