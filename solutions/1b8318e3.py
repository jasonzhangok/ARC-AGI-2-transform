def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    output = [[0 for _ in range(width)] for _ in range(height)]

    seen = [[False for _ in range(width)] for _ in range(height)]
    blocks = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5 or seen[row][col]:
                continue
            cells = []
            pending = [(row, col)]
            seen[row][col] = True
            while pending:
                current_row, current_col = pending.pop()
                cells.append((current_row, current_col))
                for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and not seen[next_row][next_col]
                            and grid[next_row][next_col] == 5):
                        seen[next_row][next_col] = True
                        pending.append((next_row, next_col))
            top = min(cell[0] for cell in cells)
            bottom = max(cell[0] for cell in cells)
            left = min(cell[1] for cell in cells)
            right = max(cell[1] for cell in cells)
            blocks.append((top, bottom, left, right))
            for cell_row, cell_col in cells:
                output[cell_row][cell_col] = 5

    points = []
    for row in range(height):
        for col in range(width):
            value = grid[row][col]
            if value == 0 or value == 5:
                continue
            minimum_distance = height + width
            for top, bottom, left, right in blocks:
                row_distance = top - row if row < top else row - bottom if row > bottom else 0
                col_distance = left - col if col < left else col - right if col > right else 0
                distance = row_distance + col_distance
                if distance < minimum_distance:
                    minimum_distance = distance
            points.append((minimum_distance, row, col, value))
    points.sort()

    for minimum_distance, row, col, value in points:
        ordered_blocks = []
        for index in range(len(blocks)):
            top, bottom, left, right = blocks[index]
            row_distance = top - row if row < top else row - bottom if row > bottom else 0
            col_distance = left - col if col < left else col - right if col > right else 0
            ordered_blocks.append((row_distance + col_distance, index))
        ordered_blocks.sort()

        placed = False
        for distance, index in ordered_blocks:
            top, bottom, left, right = blocks[index]
            row_distance = top - row if row < top else row - bottom if row > bottom else 0
            col_distance = left - col if col < left else col - right if col > right else 0
            steps = max(row_distance, col_distance) - 1
            target_row = row
            target_col = col
            if row_distance > 1:
                movement = min(steps, row_distance)
                target_row += movement if row < top else -movement
            if col_distance > 1:
                movement = min(steps, col_distance)
                target_col += movement if col < left else -movement

            candidates = [(target_row, target_col)]
            if row_distance > 0 and col_distance > 0:
                corner_row = top - 1 if row < top else bottom + 1
                corner_col = left - 1 if col < left else right + 1
                if (corner_row, corner_col) != (target_row, target_col):
                    candidates.append((corner_row, corner_col))

            for target_row, target_col in candidates:
                if (0 <= target_row < height and 0 <= target_col < width
                        and output[target_row][target_col] == 0):
                    output[target_row][target_col] = value
                    placed = True
                    break
            if placed:
                break

        if not placed and output[row][col] == 0:
            output[row][col] = value

    return output
