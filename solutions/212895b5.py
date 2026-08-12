def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    result = [row[:] for row in grid]
    block_cells = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 8:
                block_cells.append((row, col))
    if not block_cells:
        output = result
    else:
        top = min((cell[0] for cell in block_cells))
        bottom = max((cell[0] for cell in block_cells))
        left = min((cell[1] for cell in block_cells))
        right = max((cell[1] for cell in block_cells))
        center_row = (top + bottom) // 2
        center_col = (left + right) // 2
        for row_step, col_step in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            row = top - 1 if row_step < 0 else bottom + 1
            col = left - 1 if col_step < 0 else right + 1
            while 0 <= row < height and 0 <= col < width and (grid[row][col] == 0):
                result[row][col] = 2
                next_row = row + row_step
                next_col = col + col_step
                if 0 <= next_row < height and 0 <= next_col < width and (grid[next_row][col] != 0) and (grid[row][next_col] != 0):
                    break
                row = next_row
                col = next_col
        paths = ((top - 1, center_col, (-1, 0), (0, 1)), (center_row, right + 1, (0, 1), (1, 0)), (bottom + 1, center_col, (1, 0), (0, -1)), (center_row, left - 1, (0, -1), (-1, 0)))
        for row, col, outward, clockwise in paths:
            directions = (outward, clockwise)
            direction_index = 0
            segment_progress = 0
            while 0 <= row < height and 0 <= col < width and (grid[row][col] == 0):
                result[row][col] = 4
                segment_progress += 1
                if segment_progress == 2:
                    segment_progress = 0
                    direction_index = 1 - direction_index
                row += directions[direction_index][0]
                col += directions[direction_index][1]
        output = result
    return output
