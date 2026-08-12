

def transform(grid):
    """Crop to the four spanning lines and extend interior dots to a matching edge."""
    height = len(grid)
    width = len(grid[0])

    line_rows = [
        row for row in range(height)
        if all(grid[row][col] != 0 for col in range(width))
    ]
    line_cols = [
        col for col in range(width)
        if all(grid[row][col] != 0 for row in range(height))
    ]
    top, bottom = line_rows
    left, right = line_cols

    output = [row[left:right + 1] for row in grid[top:bottom + 1]]

    top_color = {}
    for cell_value in (grid[top][col] for col in range(width) if col not in line_cols):
        top_color[cell_value] = top_color.get(cell_value, 0) + 1
    top_color = max(top_color, key=top_color.get)
    bottom_color = {}
    for cell_value in (grid[bottom][col] for col in range(width) if col not in line_cols):
        bottom_color[cell_value] = bottom_color.get(cell_value, 0) + 1
    bottom_color = max(bottom_color, key=bottom_color.get)
    left_color = {}
    for cell_value in (grid[row][left] for row in range(height) if row not in line_rows):
        left_color[cell_value] = left_color.get(cell_value, 0) + 1
    left_color = max(left_color, key=left_color.get)
    right_color = {}
    for cell_value in (grid[row][right] for row in range(height) if row not in line_rows):
        right_color[cell_value] = right_color.get(cell_value, 0) + 1
    right_color = max(right_color, key=right_color.get)

    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            color = grid[row][col]
            if color == 0:
                continue

            out_row = row - top
            out_col = col - left
            if color == top_color:
                for target_row in range(1, out_row + 1):
                    output[target_row][out_col] = color
            elif color == bottom_color:
                for target_row in range(out_row, bottom - top):
                    output[target_row][out_col] = color
            elif color == left_color:
                for target_col in range(1, out_col + 1):
                    output[out_row][target_col] = color
            elif color == right_color:
                for target_col in range(out_col, right - left):
                    output[out_row][target_col] = color

    return output
