def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    seed_row = 0
    seed_col = 0
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 3:
                seed_row = row
                seed_col = col

    current_row = seed_row
    current_col = seed_col
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    length = 2
    stopped = False
    for segment in range(4 * (height + width)):
        delta_row, delta_col = directions[segment % 4]
        for _ in range(length):
            current_row += delta_row
            current_col += delta_col
            if 0 <= current_row < height and 0 <= current_col < width:
                if grid[current_row][current_col] == 2:
                    stopped = True
                    break
                output[current_row][current_col] = 3
        if stopped:
            break
        if segment % 2 == 1:
            length += 2

    return output
