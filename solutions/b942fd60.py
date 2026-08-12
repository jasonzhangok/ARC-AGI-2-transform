def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    rays = []

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2:
                continue
            if row == 0:
                rays.append((row, col, 1, 0))
            if row == height - 1:
                rays.append((row, col, -1, 0))
            if col == 0:
                rays.append((row, col, 0, 1))
            if col == width - 1:
                rays.append((row, col, 0, -1))

    processed = set()
    used_azure = set()
    cursor = 0
    while cursor < len(rays):
        row, col, row_step, col_step = rays[cursor]
        cursor += 1
        state = (row, col, row_step, col_step)
        if state in processed:
            continue
        processed.add(state)

        next_row = row + row_step
        next_col = col + col_step
        while (0 <= next_row < height and 0 <= next_col < width and
               grid[next_row][next_col] == 0):
            output[next_row][next_col] = 2
            row = next_row
            col = next_col
            next_row += row_step
            next_col += col_step

        if not (0 <= next_row < height and 0 <= next_col < width):
            continue

        obstacle = grid[next_row][next_col]
        if next_row == height - 1 and obstacle == 7:
            continue
        if obstacle == 8:
            obstacle_cell = (next_row, next_col)
            if obstacle_cell in used_azure:
                continue
            used_azure.add(obstacle_cell)

        rays.append((row, col, col_step, row_step))
        rays.append((row, col, -col_step, -row_step))

    return output
