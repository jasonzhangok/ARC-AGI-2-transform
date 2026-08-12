def transform(grid):
    height = len(grid)
    width = len(grid[0])
    grid_cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 3
    ]
    top = min(row for row, _ in grid_cells)
    bottom = max(row for row, _ in grid_cells)
    left = min(col for _, col in grid_cells)
    right = max(col for _, col in grid_cells)

    horizontal_lines = {
        row for row in range(top, bottom + 1)
        if all(grid[row][col] == 3 for col in range(left, right + 1))
    }
    vertical_lines = {
        col for col in range(left, right + 1)
        if all(grid[row][col] == 3 for row in range(top, bottom + 1))
    }

    markers = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 6
    ]
    new_top, new_bottom = top, bottom
    new_left, new_right = left, right
    for row, col in markers:
        if row < top:
            horizontal_lines.discard(new_top)
            new_top = row + 1
            horizontal_lines.add(new_top)
        if row > bottom:
            horizontal_lines.discard(new_bottom)
            new_bottom = row - 1
            horizontal_lines.add(new_bottom)
        if col < left:
            vertical_lines.discard(new_left)
            new_left = col + 1
            vertical_lines.add(new_left)
        if col > right:
            vertical_lines.discard(new_right)
            new_right = col - 1
            vertical_lines.add(new_right)

    output = [[0] * width for _ in range(height)]
    for row, col in markers:
        output[row][col] = 6
    for row in range(new_top, new_bottom + 1):
        for col in range(new_left, new_right + 1):
            if row in horizontal_lines or col in vertical_lines:
                output[row][col] = 3
    return output
