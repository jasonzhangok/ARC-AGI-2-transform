def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    blue_cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 1
    ]
    line_cells = set(blue_cells)
    for row in range(height):
        columns = [col for r, col in blue_cells if r == row]
        if 0 in columns and width - 1 in columns:
            for col in range(width):
                line_cells.add((row, col))
    for col in range(width):
        rows = [row for row, c in blue_cells if c == col]
        if 0 in rows and height - 1 in rows:
            for row in range(height):
                line_cells.add((row, col))

    visited = set()
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] != 2 or (start_row, start_col) in visited:
                continue
            component = []
            queue = [(start_row, start_col)]
            visited.add((start_row, start_col))
            queue_index = 0
            while queue_index < len(queue):
                row, col = queue[queue_index]
                queue_index += 1
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
                        and grid[next_row][next_col] == 2
                        and (next_row, next_col) not in visited
                    ):
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
            touches_line = False
            for row, col in component:
                if any(
                    cell in line_cells
                    for cell in (
                        (row, col),
                        (row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1),
                    )
                ):
                    touches_line = True
                    break
            if touches_line:
                for row, col in component:
                    output[row][col] = 1

    for row, col in line_cells:
        output[row][col] = 1

    return output
