def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    position_codes = (
        (1, 1, 1), (1, 2, 7), (1, 3, 6),
        (2, 1, 4),             (2, 3, 5),
        (3, 1, 2), (3, 2, 9), (3, 3, 3),
    )

    for top in range(height - 4):
        for left in range(width - 4):
            is_panel = True
            for row in range(5):
                for col in range(5):
                    if (row == 0 or row == 4 or col == 0 or col == 4) and grid[top + row][left + col] != 0:
                        is_panel = False
            if is_panel:
                for row, col, color in position_codes:
                    if grid[top + row][left + col] == 0:
                        output[top + row][left + col] = color
    return output
