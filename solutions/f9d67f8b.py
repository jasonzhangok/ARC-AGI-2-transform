def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 9:
                continue
            reflected_row = height + 1 - row
            reflected_col = width + 1 - col
            axial_cells = [
                (row, col),
                (reflected_row, col),
                (row, reflected_col),
                (reflected_row, reflected_col),
            ]
            intact = [
                grid[other_row][other_col]
                for other_row, other_col in axial_cells
                if 0 <= other_row < height
                and 0 <= other_col < width
                and grid[other_row][other_col] != 9
            ]
            if not intact:
                diagonal_cells = [
                    (col, row),
                    (reflected_col, row),
                    (col, reflected_row),
                    (reflected_col, reflected_row),
                ]
                intact = [
                    grid[other_row][other_col]
                    for other_row, other_col in diagonal_cells
                    if 0 <= other_row < height
                    and 0 <= other_col < width
                    and grid[other_row][other_col] != 9
                ]
            if intact:
                best_color = intact[0]
                best_count = 0
                for color in intact:
                    count = intact.count(color)
                    if count > best_count:
                        best_color = color
                        best_count = count
                output[row][col] = best_color
    return output
