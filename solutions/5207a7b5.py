def transform(grid):
    h, w = len(grid), len(grid[0])
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    length = len(cells); col = cells[0][1]
    out = [row[:] for row in grid]
    right_size = (length - 1) // 2
    for r in range(h):
        shrink = max(0, (r - length) // 2)
        left_width = max(0, col - shrink)
        for c in range(left_width): out[r][c] = 8
        right_width = (1 if right_size == 1 and r < 2
                       else max(0, right_size - (r + 1) // 2))
        for c in range(col + 1, min(w, col + 1 + right_width)): out[r][c] = 6
    output = out
    return output
