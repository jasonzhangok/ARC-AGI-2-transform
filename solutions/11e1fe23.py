def transform(grid):
    output = [row[:] for row in grid]
    points = [
        (r, c, value)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value != 0
    ]
    top, bottom = min(r for r, _, _ in points), max(r for r, _, _ in points)
    left, right = min(c for _, c, _ in points), max(c for _, c, _ in points)
    center_r, center_c = (top + bottom) // 2, (left + right) // 2
    output[center_r][center_c] = 5
    for r, c, color in points:
        rr = r + (2 if r < center_r else -2 if r > center_r else 0)
        cc = c + (2 if c < center_c else -2 if c > center_c else 0)
        output[rr][cc] = color
    return output
