def transform(grid):
    size = len(grid)
    period = 1
    direction = 1
    found = False

    for candidate_period in range(1, size):
        for candidate_direction in (1, -1):
            compared = False
            matches = True
            for row in range(size - candidate_period):
                for col in range(size):
                    shifted_col = col + candidate_direction * candidate_period
                    if 0 <= shifted_col < size:
                        compared = True
                        if grid[row][col] != grid[row + candidate_period][shifted_col]:
                            matches = False
                            break
                if not matches:
                    break
            if compared and matches:
                period = candidate_period
                direction = candidate_direction
                found = True
                break
        if found:
            break

    output_size = 2 * size
    output = [[0 for col in range(output_size)] for row in range(output_size)]
    column_offset = 0 if direction == 1 else size

    for row in range(size):
        for col in range(size):
            color = grid[row][col]
            if color == 0:
                continue
            for multiple in range(-output_size, output_size + 1):
                target_row = row + multiple * period
                target_col = column_offset + col + multiple * direction * period
                if 0 <= target_row < output_size and 0 <= target_col < output_size:
                    output[target_row][target_col] = color

    return output
