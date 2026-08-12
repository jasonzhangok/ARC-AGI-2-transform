def transform(grid):
    height, width = len(grid), len(grid[0])
    count = 0
    for r in range(height - 1):
        for c in range(width - 1):
            if all(grid[x][y] == 3 for x in (r, r + 1) for y in (c, c + 1)):
                count += 1
    result = [[0, 0, 0] for _ in range(3)]
    for index in range(min(count, 3)):
        result[index][index] = 1
    return result
