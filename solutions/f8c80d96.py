def transform(grid):
    height = len(grid)
    width = len(grid[0])
    foreground = 0
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                foreground = grid[row][col]
                break
        if foreground != 0:
            break
    visited = [[False for col in range(width)] for row in range(height)]
    components = []
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == foreground and (not visited[start_row][start_col]):
                component = []
                queue = [(start_row, start_col)]
                visited[start_row][start_col] = True
                index = 0
                while index < len(queue):
                    row, col = queue[index]
                    index += 1
                    component.append((row, col))
                    for direction in range(4):
                        if direction == 0:
                            next_row, next_col = (row - 1, col)
                        elif direction == 1:
                            next_row, next_col = (row + 1, col)
                        elif direction == 2:
                            next_row, next_col = (row, col - 1)
                        else:
                            next_row, next_col = (row, col + 1)
                        if 0 <= next_row < height and 0 <= next_col < width and (not visited[next_row][next_col]) and (grid[next_row][next_col] == foreground):
                            visited[next_row][next_col] = True
                            queue.append((next_row, next_col))
                components.append(component)
    boxes = []
    for component in components:
        top = height
        bottom = -1
        left = width
        right = -1
        cells = set(component)
        for row, col in component:
            if row < top:
                top = row
            if row > bottom:
                bottom = row
            if col < left:
                left = col
            if col > right:
                right = col
        top_side = True
        bottom_side = True
        for col in range(left, right + 1):
            if (top, col) not in cells:
                top_side = False
            if (bottom, col) not in cells:
                bottom_side = False
        left_side = True
        right_side = True
        for row in range(top, bottom + 1):
            if (row, left) not in cells:
                left_side = False
            if (row, right) not in cells:
                right_side = False
        boxes.append([top, bottom, left, right, top_side, bottom_side, left_side, right_side])
    boxes.sort()
    output = [[5 for col in range(width)] for row in range(height)]
    if len(boxes) < 2:
        for row in range(height):
            for col in range(width):
                if grid[row][col] == foreground:
                    output[row][col] = foreground
        output = output
    else:
        row_start_step = boxes[1][0] - boxes[0][0]
        row_end_step = boxes[1][1] - boxes[0][1]
        col_start_step = boxes[1][2] - boxes[0][2]
        col_end_step = boxes[1][3] - boxes[0][3]
        top_side = boxes[0][4]
        bottom_side = boxes[0][5]
        left_side = boxes[0][6]
        right_side = boxes[0][7]
        limit = height + width + 4
        for multiple in range(-limit, limit + 1):
            top = boxes[0][0] + multiple * row_start_step
            bottom = boxes[0][1] + multiple * row_end_step
            left = boxes[0][2] + multiple * col_start_step
            right = boxes[0][3] + multiple * col_end_step
            for row in range(height):
                for col in range(width):
                    on_top = top_side and row == top and (left <= col <= right)
                    on_bottom = bottom_side and row == bottom and (left <= col <= right)
                    on_left = left_side and col == left and (top <= row <= bottom)
                    on_right = right_side and col == right and (top <= row <= bottom)
                    if on_top or on_bottom or on_left or on_right:
                        output[row][col] = foreground
        output = output
    return output
