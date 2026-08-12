def transform(grid):
    height, width = len(grid), len(grid[0])
    points = [(r, c) for r in range(height) for c in range(width) if grid[r][c] != 0]
    top, bottom = min(r for r, _ in points), max(r for r, _ in points)
    left, right = min(c for _, c in points), max(c for _, c in points)
    center_row, center_col = (top + bottom) // 2, (left + right) // 2
    output = [row[:] for row in grid]
    for row, col in points:
        dr = row - center_row
        dc = col - center_col
        if dr == 0 and dc == 0:
            continue
        y, x = row, col
        while 0 <= y < height and 0 <= x < width:
            if output[y][x] == 0:
                output[y][x] = grid[row][col]
            y += dr
            x += dc
    return output
