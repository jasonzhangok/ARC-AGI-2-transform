def transform(grid):
    cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    top = min(r for r, _ in cells)
    bottom = max(r for r, _ in cells)
    left = min(c for _, c in cells)
    right = max(c for _, c in cells)
    crop = [row[left:right + 1] for row in grid[top:bottom + 1]]
    output = [row + row for row in crop]
    return output
