def transform(grid):
    output = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    for top in range(height - 2):
        for left in range(width - 2):
            block = [row[left : left + 3] for row in grid[top : top + 3]]
            if block != [[1, 1, 1], [1, 0, 1], [1, 1, 1]]:
                continue
            replacement = [[0, 2, 0], [2, 2, 2], [0, 2, 0]]
            for row in range(3):
                for col in range(3):
                    output[top + row][left + col] = replacement[row][col]
    return output
