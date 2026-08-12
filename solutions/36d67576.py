def transform(grid):
    """Copy a fully colored object's decoration to its symmetric copies."""
    height = len(grid)
    width = len(grid[0])
    result = [row[:] for row in grid]
    seen = [[False for _ in range(width)] for _ in range(height)]
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0 and (not seen[row][col]):
                component = []
                queue = [(row, col)]
                seen[row][col] = True
                cursor = 0
                while cursor < len(queue):
                    current_row, current_col = queue[cursor]
                    cursor += 1
                    component.append((current_row, current_col, grid[current_row][current_col]))
                    for next_row, next_col in ((current_row - 1, current_col), (current_row + 1, current_col), (current_row, current_col - 1), (current_row, current_col + 1)):
                        if 0 <= next_row < height and 0 <= next_col < width and (grid[next_row][next_col] != 0) and (not seen[next_row][next_col]):
                            seen[next_row][next_col] = True
                            queue.append((next_row, next_col))
                components.append(component)
    if not components:
        output = result
    else:
        template = components[0]
        most_decoration = -1
        for component in components:
            decoration_count = 0
            for row, col, color in component:
                if color != 2 and color != 4:
                    decoration_count += 1
            if decoration_count > most_decoration:
                most_decoration = decoration_count
                template = component
        symmetries = ((1, 0, 0, 1), (1, 0, 0, -1), (-1, 0, 0, 1), (-1, 0, 0, -1), (0, 1, 1, 0), (0, 1, -1, 0), (0, -1, 1, 0), (0, -1, -1, 0))
        for component in components:
            target_signature = set()
            for row, col, color in component:
                if color == 2 or color == 4:
                    target_signature.add((row, col, color))
            match = None
            for a, b, c, d in symmetries:
                source_signature = []
                for row, col, color in template:
                    if color == 2 or color == 4:
                        source_signature.append((a * row + b * col, c * row + d * col, color))
                for source_row, source_col, source_color in source_signature:
                    for target_row, target_col, target_color in target_signature:
                        if source_color == target_color:
                            row_shift = target_row - source_row
                            col_shift = target_col - source_col
                            shifted_signature = set()
                            for sig_row, sig_col, sig_color in source_signature:
                                shifted_signature.add((sig_row + row_shift, sig_col + col_shift, sig_color))
                            if shifted_signature == target_signature:
                                match = (a, b, c, d, row_shift, col_shift)
                                break
                    if match is not None:
                        break
                if match is not None:
                    break
            if match is not None:
                a, b, c, d, row_shift, col_shift = match
                for row, col, color in template:
                    if color != 2 and color != 4:
                        new_row = a * row + b * col + row_shift
                        new_col = c * row + d * col + col_shift
                        if 0 <= new_row < height and 0 <= new_col < width and (result[new_row][new_col] == 0):
                            result[new_row][new_col] = color
        output = result
    return output
