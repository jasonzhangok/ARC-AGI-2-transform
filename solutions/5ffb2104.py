def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    pieces = []
    for start_row in range(height):
        for start_col in range(width):
            color = grid[start_row][start_col]
            if color == 0 or (start_row, start_col) in seen:
                continue
            component = []
            stack = [(start_row, start_col)]
            seen.add((start_row, start_col))
            while stack:
                row, col = stack.pop()
                component.append((row, col, color))
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if 0 <= next_row < height and 0 <= next_col < width:
                        if (next_row, next_col) not in seen:
                            if grid[next_row][next_col] == color:
                                seen.add((next_row, next_col))
                                stack.append((next_row, next_col))
            pieces.append(component)

    ordered_pieces = []
    remaining_indices = set(range(len(pieces)))
    while remaining_indices:
        selected_index = None
        selected_right = -1
        for index in remaining_indices:
            right = max(col for row, col, color in pieces[index])
            if right > selected_right:
                selected_index = index
                selected_right = right
        ordered_pieces.append(pieces[selected_index])
        remaining_indices.remove(selected_index)

    output = [[0 for col in range(width)] for row in range(height)]
    for component in ordered_pieces:
        shift = 0
        can_shift = True
        while can_shift:
            for row, col, color in component:
                target_col = col + shift + 1
                if target_col >= width or output[row][target_col] != 0:
                    can_shift = False
            if can_shift:
                shift += 1
        for row, col, color in component:
            output[row][col + shift] = color

    return output
