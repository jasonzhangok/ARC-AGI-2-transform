def transform(grid):
    height = len(grid)
    width = len(grid[0])
    best_row_period = 1
    best_col_period = 1
    row_periods = []
    edge_columns = (0,) if width == 1 else (0, width - 1)
    for edge_col in edge_columns:
        best_edge_score = height + 1
        best_edge_period = 1
        for row_period in range(1, height // 2 + 1):
            mismatches = 0
            for row_phase in range(row_period):
                counts = {}
                total = 0
                for row in range(row_phase, height, row_period):
                    value = grid[row][edge_col]
                    counts[value] = counts.get(value, 0) + 1
                    total += 1
                majority = 0
                for count in counts.values():
                    if count > majority:
                        majority = count
                mismatches += total - majority
            if mismatches < best_edge_score:
                best_edge_score = mismatches
                best_edge_period = row_period
        row_periods.append(best_edge_period)
    for row_period in row_periods:
        a = best_row_period
        b = row_period
        while b:
            a, b = (b, a % b)
        best_row_period = best_row_period // a * row_period
    col_periods = []
    edge_rows = (0,) if height == 1 else (0, height - 1)
    for edge_row in edge_rows:
        best_edge_score = width + 1
        best_edge_period = 1
        for col_period in range(1, width // 2 + 1):
            mismatches = 0
            for col_phase in range(col_period):
                counts = {}
                total = 0
                for col in range(col_phase, width, col_period):
                    value = grid[edge_row][col]
                    counts[value] = counts.get(value, 0) + 1
                    total += 1
                majority = 0
                for count in counts.values():
                    if count > majority:
                        majority = count
                mismatches += total - majority
            if mismatches < best_edge_score:
                best_edge_score = mismatches
                best_edge_period = col_period
        col_periods.append(best_edge_period)
    for col_period in col_periods:
        a = best_col_period
        b = col_period
        while b:
            a, b = (b, a % b)
        best_col_period = best_col_period // a * col_period
    background = []
    for row_phase in range(best_row_period):
        tile_row = []
        for col_phase in range(best_col_period):
            counts = {}
            for row in range(row_phase, height, best_row_period):
                for col in range(col_phase, width, best_col_period):
                    value = grid[row][col]
                    counts[value] = counts.get(value, 0) + 1
            majority_value = 0
            majority_count = -1
            for value, count in counts.items():
                if count > majority_count:
                    majority_value = value
                    majority_count = count
            tile_row.append(majority_value)
        background.append(tile_row)
    foreground = {}
    for row in range(height):
        for col in range(width):
            value = grid[row][col]
            if value != background[row % best_row_period][col % best_col_period]:
                if value not in foreground:
                    foreground[value] = []
                foreground[value].append((row, col))
    rectangles = []
    for color, cells in foreground.items():
        top = height
        bottom = -1
        left = width
        right = -1
        for row, col in cells:
            if row < top:
                top = row
            if row > bottom:
                bottom = row
            if col < left:
                left = col
            if col > right:
                right = col
        rect_height = bottom - top + 1
        rect_width = right - left + 1
        is_frame = True
        for row, col in cells:
            if top < row < bottom and left < col < right:
                is_frame = False
                break
        rectangles.append((-rect_height * rect_width, -rect_height, -rect_width, color, rect_height, rect_width, is_frame))
    rectangles.sort()
    if not rectangles:
        output = []
    else:
        output_height = rectangles[0][4]
        output_width = rectangles[0][5]
        output = [[0 for col in range(output_width)] for row in range(output_height)]
        placed_top = 0
        placed_left = 0
        placed_height = output_height
        placed_width = output_width
        placed_is_frame = rectangles[0][6]
        for index in range(len(rectangles)):
            color = rectangles[index][3]
            rect_height = rectangles[index][4]
            rect_width = rectangles[index][5]
            is_frame = rectangles[index][6]
            if index == 0:
                top = 0
                left = 0
            else:
                inset = 1 if placed_is_frame else 0
                top = placed_top + placed_height - rect_height - inset
                left = placed_left + inset
            for row in range(rect_height):
                for col in range(rect_width):
                    if not is_frame or row == 0 or row == rect_height - 1 or (col == 0) or (col == rect_width - 1):
                        output[top + row][left + col] = color
            placed_top = top
            placed_left = left
            placed_height = rect_height
            placed_width = rect_width
            placed_is_frame = is_frame
        output = output
    return output
