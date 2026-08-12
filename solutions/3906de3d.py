def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [
        [0 if value == 2 else value for value in row]
        for row in grid
    ]

    for col in range(width):
        amount = sum(grid[row][col] == 2 for row in range(height))
        if amount == 0:
            continue
        encountered_one = False
        start = None
        for row in range(height):
            if grid[row][col] == 1:
                encountered_one = True
            elif encountered_one:
                start = row
                break
        if start is not None:
            for row in range(start, start + amount):
                output[row][col] = 2
    return output
