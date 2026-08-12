def transform(grid):
    h = len(grid)
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    start = next((r for r, row in enumerate(grid) if any((value != background for value in row))))
    motif = [row[:] for row in grid[start:]]
    period = len(motif)
    output = [motif[(r - start) % period][:] for r in range(h)]
    return output
