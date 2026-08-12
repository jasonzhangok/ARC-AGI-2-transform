def transform(grid):
    height = len(grid)
    width = len(grid[0])
    color_counts = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    output = [row[:] for row in grid]
    for color in color_counts:
        if color == background:
            continue
        cells = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    cells.append((row, col))
        top = min(row for row, col in cells)
        bottom = max(row for row, col in cells)
        left = min(col for row, col in cells)
        right = max(col for row, col in cells)

        same_down_diagonal = True
        same_up_diagonal = True
        first_row, first_col = cells[0]
        for row, col in cells:
            if row - col != first_row - first_col:
                same_down_diagonal = False
            if row + col != first_row + first_col:
                same_up_diagonal = False
        completed = set()
        if same_down_diagonal:
            for row in range(top, bottom + 1):
                completed.add((row, row - (first_row - first_col)))
        elif same_up_diagonal:
            for row in range(top, bottom + 1):
                completed.add((row, first_row + first_col - row))
        else:
            row_mins = []
            row_maxs = []
            rows_present = set()
            for row, col in cells:
                rows_present.add(row)
            contiguous_rows = len(rows_present) == bottom - top + 1
            for row in range(top, bottom + 1):
                columns = [col for cell_row, col in cells if cell_row == row]
                if columns:
                    row_mins.append(min(columns))
                    row_maxs.append(max(columns))
            constant_left = len(set(row_mins)) == 1
            constant_right = len(set(row_maxs)) == 1
            if contiguous_rows and (constant_left or constant_right):
                for row in range(top, bottom + 1):
                    for col in range(left, right + 1):
                        completed.add((row, col))
        for row, col in completed:
            if 0 <= row < height and 0 <= col < width:
                if grid[row][col] not in (background, color):
                    output[row][col] = color

    return output
