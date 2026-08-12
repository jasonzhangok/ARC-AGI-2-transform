def transform(grid):
    color = 0
    source_row = 0
    source_col = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                color = grid[row][col]
                source_row = row
                source_col = col

    size = 9
    output = [[0 for _ in range(size)] for _ in range(size)]
    row = 4 * source_row
    col = 4 * source_col
    output[row][col] = color
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    length = 2

    for segment in range(40):
        dr, dc = directions[segment % 4]
        for _ in range(length):
            row += dr
            col += dc
            if 0 <= row < size and 0 <= col < size:
                output[row][col] = color
        if segment % 2 == 1:
            length += 2

    return output
