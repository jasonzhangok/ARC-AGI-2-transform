def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    block_count = (width + 3) // 4
    for block in range(block_count):
        left = 4 * block
        mode = block % 3
        for row in range(height):
            for local_col in range(min(4, width - left)):
                col = left + local_col
                if grid[row][col] != 0:
                    continue
                if mode == 0 and local_col < row:
                    output[row][col] = 4
                elif mode == 1 and row < local_col <= 3 - row:
                    output[row][col] = 4
                elif mode == 2 and row == 2 and local_col == 3:
                    output[row][col] = 4
    return output
