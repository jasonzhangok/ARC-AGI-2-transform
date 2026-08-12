def transform(grid):
    result = [row[:] for row in grid]
    horizontal = [r for r, row in enumerate(grid) if all(value == 8 for value in row)]
    vertical = [c for c in range(len(grid[0])) if all(grid[r][c] == 8 for r in range(len(grid)))]
    row_ranges = [(0, horizontal[0]), (horizontal[0] + 1, horizontal[1]), (horizontal[1] + 1, len(grid))]
    col_ranges = [(0, vertical[0]), (vertical[0] + 1, vertical[1]), (vertical[1] + 1, len(grid[0]))]
    colors = {(0, 1): 2, (1, 0): 4, (1, 1): 6, (1, 2): 3, (2, 1): 1}
    for (row_band, col_band), color in colors.items():
        top, bottom = row_ranges[row_band]
        left, right = col_ranges[col_band]
        for r in range(top, bottom):
            for c in range(left, right):
                result[r][c] = color
    return result
