def transform(grid):
    top_of_container = min(
        row
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 5
    )
    top_of_fill = min(
        row
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 8
    )
    amount = top_of_fill - top_of_container

    spiral = [
        (0, 0), (0, 1), (0, 2),
        (1, 2), (2, 2), (2, 1),
        (2, 0), (1, 0), (1, 1),
    ]
    output = [[0, 0, 0] for _ in range(3)]
    for row, col in spiral[:amount]:
        output[row][col] = 8
    return output
