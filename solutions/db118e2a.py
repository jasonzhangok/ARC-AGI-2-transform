def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = 7
    frame = next(value for value in grid[0] if value != background)

    anomalies = [
        (row, column)
        for row in range(1, height - 1)
        for column in range(1, width - 1)
        if grid[row][column] != background
    ]
    row_sum = sum(row for row, column in anomalies)
    column_sum = sum(column for row, column in anomalies)
    count = len(anomalies)
    choices = []
    for top in range(1, height - 3):
        for left in range(1, width - 3):
            if all(
                top <= row <= top + 2 and left <= column <= left + 2
                for row, column in anomalies
            ):
                distance = (
                    abs((top + 1) * count - row_sum)
                    + abs((left + 1) * count - column_sum)
                )
                choices.append((distance, top, left))
    _, top, left = min(choices)

    tile = [[background for _ in range(5)] for _ in range(5)]
    for index in range(1, 4):
        tile[0][index] = frame
        tile[4][index] = frame
        tile[index][0] = frame
        tile[index][4] = frame
    for row in range(3):
        for column in range(3):
            tile[row + 1][column + 1] = grid[top + row][left + column]

    output = [[background for _ in range(15)] for _ in range(15)]
    for base_row, base_column in ((2, 2), (8, 8)):
        for row in range(5):
            for column in range(5):
                output[base_row + row][base_column + column] = tile[row][column]

    return output
