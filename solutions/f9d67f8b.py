def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 9:
                continue
            reflected_rows = {row, height + 1 - row}
            reflected_cols = {col, width + 1 - col}
            intact = [
                grid[other_row][other_col]
                for other_row in reflected_rows
                for other_col in reflected_cols
                if 0 <= other_row < height
                and 0 <= other_col < width
                and grid[other_row][other_col] != 9
            ]
            if intact:
                output[row][col] = intact[0]
    return output
