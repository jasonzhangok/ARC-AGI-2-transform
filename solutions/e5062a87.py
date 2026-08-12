def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    template_cells = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 2:
                template_cells.append((row, col))

    top = min(row for row, col in template_cells)
    bottom = max(row for row, col in template_cells)
    left = min(col for row, col in template_cells)
    right = max(col for row, col in template_cells)
    box_height = bottom - top + 1
    box_width = right - left + 1
    shape = {(row - top, col - left) for row, col in template_cells}
    support = {(row, col) for row in range(box_height) for col in range(box_width) if grid[top + row][left + col] == 5}

    support_variants = []
    for symmetry in range(8):
        mapping = {}
        usable = True
        for row in range(box_height):
            for col in range(box_width):
                if symmetry == 0:
                    transformed = (row, col)
                elif symmetry == 1:
                    transformed = (box_height - 1 - row, col)
                elif symmetry == 2:
                    transformed = (row, box_width - 1 - col)
                elif symmetry == 3:
                    transformed = (box_height - 1 - row, box_width - 1 - col)
                elif box_height == box_width:
                    if symmetry == 4:
                        transformed = (col, box_height - 1 - row)
                    elif symmetry == 5:
                        transformed = (box_width - 1 - col, row)
                    elif symmetry == 6:
                        transformed = (col, row)
                    else:
                        transformed = (box_height - 1 - col, box_width - 1 - row)
                else:
                    usable = False
                    break
                mapping[(row, col)] = transformed
            if not usable:
                break
        if usable and {mapping[cell] for cell in shape} == shape:
            transformed_support = {mapping[cell] for cell in support}
            if transformed_support not in support_variants:
                support_variants.append(transformed_support)

    candidates = []
    for start_row in range(height - box_height + 1):
        for start_col in range(width - box_width + 1):
            cells = {(start_row + row, start_col + col) for row, col in shape}
            if not all(grid[row][col] == 0 for row, col in cells):
                continue
            if support:
                score = 0
                for variant in support_variants:
                    if all(grid[start_row + row][start_col + col] == 5 for row, col in variant):
                        score += 1
            else:
                score = 1
            if score > 0:
                candidates.append((-score, start_row, start_col, cells))

    if (box_height == 1 or box_width == 1) and candidates:
        nearest = min(abs(start_row - top) + abs(start_col - left) for negative_score, start_row, start_col, cells in candidates)
        candidates = [candidate for candidate in candidates if abs(candidate[1] - top) + abs(candidate[2] - left) == nearest]

    candidates.sort()
    occupied = set()
    for negative_score, start_row, start_col, cells in candidates:
        if cells & occupied:
            continue
        occupied |= cells
        for row, col in cells:
            output[row][col] = 2

    return output
