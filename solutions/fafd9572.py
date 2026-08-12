def transform(grid):
    output = [row[:] for row in grid]
    height = len(grid)
    width = len(grid[0]) if height else 0
    legend_cells = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] not in (0, 1):
                legend_cells.append((row, col))
    if not legend_cells:
        return output
    top = min(row for row, col in legend_cells)
    bottom = max(row for row, col in legend_cells)
    left = min(col for row, col in legend_cells)
    right = max(col for row, col in legend_cells)
    motif_height = bottom - top + 1
    motif_width = right - left + 1
    mask = []
    legend = {}
    for row, col in legend_cells:
        relative = (row - top, col - left)
        mask.append(relative)
        legend[relative] = grid[row][col]
    copies = []
    for top_row in range(height - motif_height + 1):
        for left_col in range(width - motif_width + 1):
            matches = True
            for row in range(motif_height):
                for col in range(motif_width):
                    is_mask_cell = (row, col) in mask
                    if (grid[top_row + row][left_col + col] == 1) != is_mask_cell:
                        matches = False
            if matches:
                copies.append((top_row, left_col))
    copy_rows = sorted(set(row for row, col in copies))
    copy_cols = sorted(set(col for row, col in copies))
    for top_row, left_col in copies:
        position = (copy_rows.index(top_row), copy_cols.index(left_col))
        if position in legend:
            color = legend[position]
            for row, col in mask:
                output[top_row + row][left_col + col] = color
    return output
