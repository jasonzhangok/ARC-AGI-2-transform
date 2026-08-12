def transform(grid):
    nonzero = sum(value != 0 for row in grid for value in row)
    blocks_per_side = 9 - nonzero
    side = 3 * blocks_per_side
    output = [[0] * side for _ in range(side)]
    for index in range(nonzero):
        br, bc = divmod(index, blocks_per_side)
        for r in range(3):
            for c in range(3):
                output[3 * br + r][3 * bc + c] = grid[r][c]
    return output
