def transform(grid):
    height, width = len(grid), len(grid[0])
    marked = set()
    for row in range(height - 4):
        for col in range(width - 4):
            color = grid[row][col]
            if color != 0 and all(grid[row + dr][col + dc] == color for dr in range(5) for dc in range(5)):
                marked |= {(row + dr, col + dc) for dr in range(5) for dc in range(5)}
    output = [row[:] for row in grid]
    for row, col in marked:
        output[row][col] = 4
    return output
