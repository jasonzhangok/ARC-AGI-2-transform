def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    for r in range(height - 1):
        for c in range(width - 1):
            cells = [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]
            if sum(grid[x][y] == 8 for x, y in cells) == 3:
                for x, y in cells:
                    if grid[x][y] == 0:
                        result[x][y] = 1
    output = result
    return output
