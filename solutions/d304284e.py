def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    foreground = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                foreground.append((row, col))
    if not foreground:
        output = [row[:] for row in grid]
    else:
        top = min((point[0] for point in foreground))
        bottom = max((point[0] for point in foreground))
        left = min((point[1] for point in foreground))
        right = max((point[1] for point in foreground))
        shape_height = bottom - top + 1
        shape_width = right - left + 1
        mask = []
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if grid[row][col] != 0:
                    mask.append((row - top, col - left))
        output = [[0 for _ in range(width)] for _ in range(height)]
        copy_index = 0
        copy_left = left
        while copy_left < width:
            color = 6 if copy_index % 3 == 2 else 7
            copy_top = top
            while copy_top < height:
                for row_offset, col_offset in mask:
                    target_row = copy_top + row_offset
                    target_col = copy_left + col_offset
                    if target_row < height and target_col < width:
                        output[target_row][target_col] = color
                if color != 6:
                    break
                copy_top += shape_height + 1
            copy_index += 1
            copy_left += shape_width + 1
        output = output
    return output
