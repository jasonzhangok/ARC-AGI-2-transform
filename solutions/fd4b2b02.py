def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [[0 for _ in range(width)] for _ in range(height)]
    points = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                points.append((row, col, grid[row][col]))

    color = points[0][2]
    other_color = 6 if color == 3 else 3
    seed_top = min(row for row, col, value in points)
    seed_bottom = max(row for row, col, value in points)
    seed_left = min(col for row, col, value in points)
    seed_right = max(col for row, col, value in points)
    seed_height = seed_bottom - seed_top + 1
    seed_width = seed_right - seed_left + 1

    for row_sign in (-1, 1):
        for col_sign in (-1, 1):
            top = seed_top
            left = seed_left
            rectangle_height = seed_height
            rectangle_width = seed_width
            rectangle_color = color
            while True:
                for row in range(max(0, top), min(height, top + rectangle_height)):
                    for col in range(max(0, left), min(width, left + rectangle_width)):
                        output[row][col] = rectangle_color

                next_height = rectangle_width
                next_width = rectangle_height
                if row_sign < 0:
                    next_top = top - next_height
                else:
                    next_top = top + rectangle_height
                if col_sign < 0:
                    next_left = left - next_width
                else:
                    next_left = left + rectangle_width

                top = next_top
                left = next_left
                rectangle_height = next_height
                rectangle_width = next_width
                rectangle_color = other_color if rectangle_color == color else color
                if ((row_sign < 0 and top + rectangle_height <= 0) or
                        (row_sign > 0 and top >= height) or
                        (col_sign < 0 and left + rectangle_width <= 0) or
                        (col_sign > 0 and left >= width)):
                    break

    return output
