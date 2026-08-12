def transform(grid):
    height, width = len(grid), len(grid[0])
    ones = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 1]
    sixes = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 6]
    output = [[8] * width for _ in range(height)]
    for row, col in ones:
        output[row][col] = 1
        partner = next((point for point in sixes if point[0] == row or point[1] == col), None)
        if partner is None:
            continue
        dr, dc = partner[0] - row, partner[1] - col
        target_row, target_col = row - dc, col + dr
        if 0 <= target_row < height and 0 <= target_col < width:
            output[target_row][target_col] = 7
    return output
