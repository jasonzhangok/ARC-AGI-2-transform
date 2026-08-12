def transform(grid):
    points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    top, bottom = min(r for r, _ in points), max(r for r, _ in points)
    left, right = min(c for _, c in points), max(c for _, c in points)
    out_height = (bottom - top + 1) // 2
    out_width = (right - left + 1) // 2
    return [row[left:left + out_width] for row in grid[top:top + out_height]]
