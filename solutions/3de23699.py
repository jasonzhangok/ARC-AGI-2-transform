def transform(grid):
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    marker = min(counts, key=counts.get)
    points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == marker]
    top, bottom = (min((r for r, _ in points)), max((r for r, _ in points)))
    left, right = (min((c for _, c in points)), max((c for _, c in points)))
    output = [[marker if grid[r][c] != 0 else 0 for c in range(left + 1, right)] for r in range(top + 1, bottom)]
    return output
