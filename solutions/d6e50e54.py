def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    square_cells = []
    markers = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                square_cells.append((row, col))
            elif grid[row][col] == 9:
                markers.append((row, col))

    top = min(row for row, col in square_cells)
    bottom = max(row for row, col in square_cells)
    left = min(col for row, col in square_cells)
    right = max(col for row, col in square_cells)
    projected = []

    for row, col in markers:
        if top <= row <= bottom:
            if col < left:
                projected.append((left - col, row, col, 0))
            else:
                projected.append((col - right, row, col, 1))
        elif row < top:
            projected.append((top - row, row, col, 2))
        else:
            projected.append((row - bottom, row, col, 3))

    nearest = min(item[0] for item in projected)
    for row, col in square_cells:
        output[row][col] = 2
    for distance, row, col, side in projected:
        output[row][col] = 7
        on_boundary = distance == nearest
        if side == 0:
            target_row = row
            target_col = left if on_boundary else left - 1
        elif side == 1:
            target_row = row
            target_col = right if on_boundary else right + 1
        elif side == 2:
            target_row = top if on_boundary else top - 1
            target_col = col
        else:
            target_row = bottom if on_boundary else bottom + 1
            target_col = col
        output[target_row][target_col] = 9

    return output
