def transform(grid):
    height = len(grid)
    width = len(grid[0])

    anchor = next(
        (row, column)
        for row in range(height)
        for column in range(width)
        if grid[row][column] == 3
    )
    offsets = [
        (row - anchor[0], column - anchor[1])
        for row in range(height)
        for column in range(width)
        if grid[row][column] == 8
    ]
    targets = [
        (row, column)
        for row in range(height)
        for column in range(width)
        if grid[row][column] == 2
    ]

    output = [[0 for _ in range(width)] for _ in range(height)]
    for target_row, target_column in targets:
        for row_offset, column_offset in offsets:
            row = target_row + row_offset
            column = target_column + column_offset
            if 0 <= row < height and 0 <= column < width:
                output[row][column] = 8

    return output
