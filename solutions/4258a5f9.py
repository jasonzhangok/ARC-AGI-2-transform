def transform(grid):
    height, width = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    markers = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5]
    for r, c in markers:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and result[nr][nc] == 0:
                    result[nr][nc] = 1
    output = result
    return output
