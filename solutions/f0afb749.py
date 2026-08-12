def transform(grid):
    diagonals = {
        row - col
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] != 0
    }
    output = []
    for row in range(len(grid)):
        first = []
        second = []
        for col in range(len(grid[0])):
            value = grid[row][col]
            if value != 0:
                first.extend((value, value))
                second.extend((value, value))
            elif row - col in diagonals:
                first.extend((1, 0))
                second.extend((0, 1))
            else:
                first.extend((0, 0))
                second.extend((0, 0))
        output.extend((first, second))
    return output
