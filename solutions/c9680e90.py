def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    divider = 0
    for row in range(height):
        if all(grid[row][col] == 9 for col in range(width)):
            divider = row
            break

    output = [[7 for _ in range(width)] for _ in range(height)]
    for col in range(width):
        output[divider][col] = 9

    for row in range(divider + 1, height):
        for col in range(width):
            if grid[row][col] != 2:
                continue
            end_row = row
            end_col = col
            direction_row = 0
            direction_col = 0
            for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_row = row + delta_row
                next_col = col + delta_col
                if (
                    divider < next_row < height
                    and 0 <= next_col < width
                    and grid[next_row][next_col] == 6
                ):
                    direction_row = delta_row
                    direction_col = delta_col
                    break
            while direction_row != 0 or direction_col != 0:
                next_row = end_row + direction_row
                next_col = end_col + direction_col
                if (
                    not (divider < next_row < height and 0 <= next_col < width)
                    or grid[next_row][next_col] != 6
                ):
                    break
                end_row = next_row
                end_col = next_col

            output[end_row][end_col] = 2
            mirror_row = 2 * divider - end_row
            if 0 <= mirror_row < divider:
                output[mirror_row][end_col] = 5

    return output
