def transform(grid):
    nonzero = [
        (row, col)
        for row in range(3)
        for col in range(3)
        if grid[row][col] != 0
    ]
    top = min(row for row, _ in nonzero)
    left = min(col for _, col in nonzero)
    side = sum(value == 3 for row in grid for value in row) + 1
    output = [[0] * 9 for _ in range(9)]
    for block in range(2):
        block_top = top + block * side
        block_left = left + block * side
        for row in range(block_top, block_top + side):
            for col in range(block_left, block_left + side):
                if 0 <= row < 9 and 0 <= col < 9:
                    output[row][col] = 3
    return output
