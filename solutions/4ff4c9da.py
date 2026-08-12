def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = sorted(
        {
            value
            for row in grid
            for value in row
            if value != 0 and value != 8
        }
    )
    best_pixels = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 8
    }

    for color in colors:
        seen = set()
        marked_shapes = []
        valid_color = True

        for start_row in range(height):
            for start_col in range(width):
                if (
                    (start_row, start_col) in seen
                    or grid[start_row][start_col] != color
                    and grid[start_row][start_col] != 8
                ):
                    continue

                component = [(start_row, start_col)]
                seen.add((start_row, start_col))
                index = 0
                has_mark = False

                while index < len(component):
                    row, col = component[index]
                    index += 1
                    if grid[row][col] == 8:
                        has_mark = True

                    for row_step in (-1, 0, 1):
                        for col_step in (-1, 0, 1):
                            next_row = row + row_step
                            next_col = col + col_step
                            if (
                                (row_step != 0 or col_step != 0)
                                and 0 <= next_row < height
                                and 0 <= next_col < width
                                and (next_row, next_col) not in seen
                                and (
                                    grid[next_row][next_col] == color
                                    or grid[next_row][next_col] == 8
                                )
                            ):
                                seen.add((next_row, next_col))
                                component.append((next_row, next_col))

                if has_mark:
                    if any(grid[row][col] != 8 for row, col in component):
                        valid_color = False
                        break
                    top = min(row for row, col in component)
                    left = min(col for row, col in component)
                    shape = tuple(
                        sorted((row - top, col - left) for row, col in component)
                    )
                    if shape not in marked_shapes:
                        marked_shapes.append(shape)
            if not valid_color:
                break

        if not valid_color or not marked_shapes:
            continue

        seen = set()
        candidate_pixels = set()
        for start_row in range(height):
            for start_col in range(width):
                if (
                    (start_row, start_col) in seen
                    or grid[start_row][start_col] != color
                    and grid[start_row][start_col] != 8
                ):
                    continue

                component = [(start_row, start_col)]
                seen.add((start_row, start_col))
                index = 0
                while index < len(component):
                    row, col = component[index]
                    index += 1
                    for row_step in (-1, 0, 1):
                        for col_step in (-1, 0, 1):
                            next_row = row + row_step
                            next_col = col + col_step
                            if (
                                (row_step != 0 or col_step != 0)
                                and 0 <= next_row < height
                                and 0 <= next_col < width
                                and (next_row, next_col) not in seen
                                and (
                                    grid[next_row][next_col] == color
                                    or grid[next_row][next_col] == 8
                                )
                            ):
                                seen.add((next_row, next_col))
                                component.append((next_row, next_col))

                top = min(row for row, col in component)
                left = min(col for row, col in component)
                shape = tuple(
                    sorted((row - top, col - left) for row, col in component)
                )
                if shape in marked_shapes:
                    candidate_pixels.update(component)

        if len(candidate_pixels) > len(best_pixels):
            best_pixels = candidate_pixels

    output = [row[:] for row in grid]
    for row, col in best_pixels:
        output[row][col] = 8
    return output
