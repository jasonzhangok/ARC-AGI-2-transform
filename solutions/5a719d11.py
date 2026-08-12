def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    groups = []
    row = 0
    while row < height:
        if all(value == 0 for value in grid[row]):
            row += 1
            continue
        top = row
        while row < height and any(grid[row]):
            row += 1
        groups.append((top, row))

    for top, bottom in groups:
        zero_columns = []
        for col in range(width):
            if all(grid[row][col] == 0 for row in range(top, bottom)):
                zero_columns.append(col)
        divider_left = zero_columns[0]
        divider_right = zero_columns[-1]
        panel_width = divider_left
        right_start = divider_right + 1

        left_counts = {}
        right_counts = {}
        for row in range(top, bottom):
            for col in range(panel_width):
                color = grid[row][col]
                left_counts[color] = left_counts.get(color, 0) + 1
                color = grid[row][right_start + col]
                right_counts[color] = right_counts.get(color, 0) + 1
        left_background = 0
        left_background_count = -1
        for color in left_counts:
            if left_counts[color] > left_background_count:
                left_background = color
                left_background_count = left_counts[color]
        right_background = 0
        right_background_count = -1
        for color in right_counts:
            if right_counts[color] > right_background_count:
                right_background = color
                right_background_count = right_counts[color]

        left_mask = set()
        right_mask = set()
        for row in range(top, bottom):
            for col in range(panel_width):
                if grid[row][col] != left_background:
                    left_mask.add((row - top, col))
                if grid[row][right_start + col] != right_background:
                    right_mask.add((row - top, col))
        for row in range(top, bottom):
            for col in range(panel_width):
                if (row - top, col) in right_mask:
                    output[row][col] = right_background
                else:
                    output[row][col] = left_background
                if (row - top, col) in left_mask:
                    output[row][right_start + col] = left_background
                else:
                    output[row][right_start + col] = right_background

    return output
