def transform(grid):
    logical = [row[1::2] for row in grid[1::2]]
    logical_height, logical_width = len(logical), len(logical[0])
    inner_size = 22
    gap = 2
    block_height = (inner_size - gap * (logical_height - 1)) // logical_height
    block_width = (inner_size - gap * (logical_width - 1)) // logical_width
    output = [[0] * 26 for _ in range(26)]
    horizontal_component = {}
    remaining = {
        (row, col)
        for row in range(logical_height)
        for col in range(logical_width)
        if logical[row][col] != 0
    }
    while remaining:
        start = remaining.pop()
        color = logical[start[0]][start[1]]
        queue = [start]
        component = []
        for row, col in queue:
            component.append((row, col))
            for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = row + row_step, col + col_step
                if neighbor in remaining and logical[neighbor[0]][neighbor[1]] == color:
                    remaining.remove(neighbor)
                    queue.append(neighbor)
        has_horizontal_pair = any(
            (row, col + 1) in component for row, col in component
        )
        for cell in component:
            horizontal_component[cell] = has_horizontal_pair

    for logical_row in range(logical_height):
        top = 2 + logical_row * (block_height + gap)
        for logical_col in range(logical_width):
            left = 2 + logical_col * (block_width + gap)
            color = logical[logical_row][logical_col]
            if color == 0:
                continue
            for row in range(top, top + block_height):
                for col in range(left, left + block_width):
                    output[row][col] = color

            if (horizontal_component[(logical_row, logical_col)] and
                    logical_col + 1 < logical_width and
                    logical[logical_row][logical_col + 1] == color):
                for row in range(top, top + block_height):
                    for col in range(left + block_width,
                                     left + block_width + gap):
                        output[row][col] = color
            if (not horizontal_component[(logical_row, logical_col)] and
                    logical_row + 1 < logical_height and
                    logical[logical_row + 1][logical_col] == color):
                for row in range(top + block_height,
                                 top + block_height + gap):
                    for col in range(left, left + block_width):
                        output[row][col] = color
    return output
