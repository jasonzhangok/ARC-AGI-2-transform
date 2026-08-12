def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    seeds = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 3]
    for row, column in seeds:
        for c in range(column - 2, column + 3):
            if 0 <= row - 2 < height and 0 <= c < width:
                result[row - 2][c] = 5
            if 0 <= row + 2 < height and 0 <= c < width:
                result[row + 2][c] = 8
        for r in range(row - 1, row + 2):
            for c in (column - 2, column + 2):
                if 0 <= r < height and 0 <= c < width:
                    result[r][c] = 2
        if 0 <= row - 1 < height:
            result[row - 1][column] = 5
        if 0 <= row + 2 < height:
            for c in range(width):
                if not (column - 2 <= c <= column + 2):
                    result[row + 2][c] = 2
    return result
