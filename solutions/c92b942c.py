def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    output_height = height * 3
    output_width = width * 3
    output = [
        [grid[row % height][col % width] for col in range(output_width)]
        for row in range(output_height)
    ]
    colored_cells = []

    for row in range(output_height):
        active = False
        for col in range(output_width):
            if output[row][col] != 0:
                active = True
                colored_cells.append((row, col))
        if active:
            for col in range(output_width):
                if output[row][col] == 0:
                    output[row][col] = 1

    for row, col in colored_cells:
        for next_row, next_col in ((row - 1, col - 1), (row + 1, col + 1)):
            if (
                0 <= next_row < output_height
                and 0 <= next_col < output_width
                and output[next_row][next_col] == 0
            ):
                output[next_row][next_col] = 3

    return output
