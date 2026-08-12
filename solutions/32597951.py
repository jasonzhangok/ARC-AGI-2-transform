def transform(grid):
    cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 8]
    top = min(r for r, _ in cells)
    bottom = max(r for r, _ in cells)
    left = min(c for _, c in cells)
    right = max(c for _, c in cells)
    result = [row[:] for row in grid]
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if result[r][c] == 1:
                result[r][c] = 3
    output = result
    return output
