def transform(grid):
    background = {}
    for cell_value in (v for row in grid for v in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    cells = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v != background]
    n = len(cells)
    top_r, top_c = min(cells)
    out = [[background] * len(grid[0]) for _ in grid]
    for step in range(1, n + 2):
        r, c = (top_r - step, top_c + step)
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            out[r][c] = grid[cells[0][0]][cells[0][1]]
    output = out
    return output
