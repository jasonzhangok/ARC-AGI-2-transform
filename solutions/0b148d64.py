def transform(grid):
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    selected = min(counts, key=counts.get)
    points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == selected]
    top, bottom = (min((r for r, _ in points)), max((r for r, _ in points)))
    left, right = (min((c for _, c in points)), max((c for _, c in points)))
    output = [[selected if grid[r][c] == selected else 0 for c in range(left, right + 1)] for r in range(top, bottom + 1)]
    return output
