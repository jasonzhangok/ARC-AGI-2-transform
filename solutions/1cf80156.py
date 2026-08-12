def transform(grid):
    points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    top, bottom = min(r for r, _ in points), max(r for r, _ in points)
    left, right = min(c for _, c in points), max(c for _, c in points)
    output = [row[left:right + 1] for row in grid[top:bottom + 1]]
    return output
