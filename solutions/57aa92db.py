def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    output = [row[:] for row in grid]
    seen = set()
    components = []

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0 or (start_row, start_col) in seen:
                continue
            pending = [(start_row, start_col)]
            seen.add((start_row, start_col))
            component = []
            while pending:
                row, col = pending.pop()
                component.append((row, col))
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and grid[next_row][next_col] != 0
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        pending.append((next_row, next_col))
            components.append(component)

    reference = None
    primary_color = None
    special_color = None
    for component in components:
        counts = {}
        for row, col in component:
            color = grid[row][col]
            counts[color] = counts.get(color, 0) + 1
        if len(counts) != 2:
            continue
        ordered = list(counts)
        if counts[ordered[0]] > counts[ordered[1]]:
            ordered[0], ordered[1] = ordered[1], ordered[0]
        if counts[ordered[0]] == 1 and counts[ordered[1]] > 1:
            reference = component
            special_color = ordered[0]
            primary_color = ordered[1]
            break

    if reference is None:
        return output

    reference_top = min(row for row, col in reference)
    reference_bottom = max(row for row, col in reference)
    reference_left = min(col for row, col in reference)
    reference_right = max(col for row, col in reference)
    pattern = [
        grid[row][reference_left:reference_right + 1]
        for row in range(reference_top, reference_bottom + 1)
    ]
    special_row = 0
    special_col = 0
    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            if pattern[row][col] == special_color:
                special_row = row
                special_col = col

    for component in components:
        if component is reference:
            continue
        colors = {grid[row][col] for row, col in component}
        if len(colors) != 2 or special_color not in colors:
            continue
        replacement_color = next(color for color in colors if color != special_color)
        special_cells = [
            (row, col)
            for row, col in component
            if grid[row][col] == special_color
        ]
        block_top = min(row for row, col in special_cells)
        block_bottom = max(row for row, col in special_cells)
        block_left = min(col for row, col in special_cells)
        block_right = max(col for row, col in special_cells)
        scale = block_bottom - block_top + 1
        if (
            block_right - block_left + 1 != scale
            or len(special_cells) != scale * scale
        ):
            continue

        copy_top = block_top - special_row * scale
        copy_left = block_left - special_col * scale
        for pattern_row in range(len(pattern)):
            for pattern_col in range(len(pattern[0])):
                value = pattern[pattern_row][pattern_col]
                if value != primary_color and value != special_color:
                    continue
                color = special_color if value == special_color else replacement_color
                for row_offset in range(scale):
                    for col_offset in range(scale):
                        row = copy_top + pattern_row * scale + row_offset
                        col = copy_left + pattern_col * scale + col_offset
                        if 0 <= row < height and 0 <= col < width:
                            output[row][col] = color

    return output
