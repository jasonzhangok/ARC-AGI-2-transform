def transform(grid):
    count = 0
    for row in range(len(grid) - 1):
        for col in range(len(grid[0]) - 1):
            if all(grid[row + dr][col + dc] == 1 for dr in (0, 1) for dc in (0, 1)):
                count += 1
    output = [[1] * count + [0] * (5 - count)]
    return output
