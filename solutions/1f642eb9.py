def transform(grid):
    height, width = len(grid), len(grid[0])
    eights = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 8]
    top, bottom = min(r for r, _ in eights), max(r for r, _ in eights)
    left, right = min(c for _, c in eights), max(c for _, c in eights)
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color in (0, 8):
                continue
            if top <= row <= bottom:
                target_col = left if col < left else right if col > right else col
                output[row][target_col] = color
            if left <= col <= right:
                target_row = top if row < top else bottom if row > bottom else row
                output[target_row][col] = color
    return output
