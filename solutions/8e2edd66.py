

def transform(grid):
    color = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        color[cell_value] = color.get(cell_value, 0) + 1
    color = max(color, key=color.get)
    inverse = [[color if value == 0 else 0 for value in row] for row in grid]
    output = [[0] * 9 for _ in range(9)]
    for br in range(3):
        for bc in range(3):
            if grid[br][bc] == 0:
                for r in range(3):
                    for c in range(3):
                        output[3 * br + r][3 * bc + c] = inverse[r][c]
    return output
