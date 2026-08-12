def transform(grid):
    height = len(grid)
    width = len(grid[0])
    one_cells = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                one_cells.append((row, col))
    template_top = min(row for row, col in one_cells)
    template_bottom = max(row for row, col in one_cells)
    template_left = min(col for row, col in one_cells)
    template_right = max(col for row, col in one_cells)
    expanded = True
    while expanded:
        expanded = False
        if template_top > 0:
            full_side = True
            for col in range(template_left, template_right + 1):
                if grid[template_top - 1][col] != 4:
                    full_side = False
                    break
            if full_side:
                template_top -= 1
                expanded = True
        if template_bottom + 1 < height:
            full_side = True
            for col in range(template_left, template_right + 1):
                if grid[template_bottom + 1][col] != 4:
                    full_side = False
                    break
            if full_side:
                template_bottom += 1
                expanded = True
        if template_left > 0:
            full_side = True
            for row in range(template_top, template_bottom + 1):
                if grid[row][template_left - 1] != 4:
                    full_side = False
                    break
            if full_side:
                template_left -= 1
                expanded = True
        if template_right + 1 < width:
            full_side = True
            for row in range(template_top, template_bottom + 1):
                if grid[row][template_right + 1] != 4:
                    full_side = False
                    break
            if full_side:
                template_right += 1
                expanded = True
    template_height = template_bottom - template_top + 1
    template_width = template_right - template_left + 1
    motif = set()
    for row in range(template_top, template_bottom + 1):
        for col in range(template_left, template_right + 1):
            if grid[row][col] == 4:
                motif.add((row - template_top, col - template_left))

    orientations = []
    current_height = template_height
    current_width = template_width
    current_motif = motif
    for _ in range(4):
        key = (current_height, current_width, tuple(sorted(current_motif)))
        if key not in orientations:
            orientations.append(key)
        rotated = set()
        for row, col in current_motif:
            rotated.add((col, current_height - 1 - row))
        current_motif = rotated
        current_height, current_width = current_width, current_height

    output = [row[:] for row in grid]
    for shape_height, shape_width, motif_tuple in orientations:
        shape_motif = set(motif_tuple)
        for top in range(-shape_height + 1, height):
            for left in range(-shape_width + 1, width):
                valid = True
                for row, col in shape_motif:
                    canvas_row = top + row
                    canvas_col = left + col
                    if not (0 <= canvas_row < height and 0 <= canvas_col < width and grid[canvas_row][canvas_col] == 4):
                        valid = False
                        break
                if not valid:
                    continue
                for row in range(shape_height):
                    if not valid:
                        break
                    for col in range(shape_width):
                        canvas_row = top + row
                        canvas_col = left + col
                        if 0 <= canvas_row < height and 0 <= canvas_col < width and (row, col) not in shape_motif and grid[canvas_row][canvas_col] == 4:
                            valid = False
                            break
                if not valid:
                    continue
                for row in range(shape_height):
                    for col in range(shape_width):
                        canvas_row = top + row
                        canvas_col = left + col
                        if 0 <= canvas_row < height and 0 <= canvas_col < width and (row, col) not in shape_motif and output[canvas_row][canvas_col] == 0:
                            output[canvas_row][canvas_col] = 1
    return output
