def transform(grid):
    height = len(grid)
    width = len(grid[0])
    source = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 8:
                source.append((r, c))

    top = min(r for r, c in source)
    bottom = max(r for r, c in source)
    left = min(c for r, c in source)
    right = max(c for r, c in source)
    output = [row[:] for row in grid]

    for r in range(top, bottom + 1):
        for c in range(left - 1, -1, -1):
            if grid[r][c] == 1:
                break
            output[r][c] = 4
        for c in range(right + 1, width):
            if grid[r][c] == 1:
                break
            output[r][c] = 4

    for c in range(left, right + 1):
        for r in range(top - 1, -1, -1):
            if grid[r][c] == 1:
                break
            output[r][c] = 4
        for r in range(bottom + 1, height):
            if grid[r][c] == 1:
                break
            output[r][c] = 4

    return output
