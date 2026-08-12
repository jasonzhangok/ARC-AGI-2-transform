

def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    markers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    rows = sorted(r for r, _ in markers)
    cols = sorted(c for _, c in markers)
    r0, r1 = rows[0] + 1, rows[-1] - 1
    c0, c1 = cols[0] + 1, cols[-1] - 1
    color = {}
    for cell_value in (value for row in grid for value in row if value not in (0, 5)):
        color[cell_value] = color.get(cell_value, 0) + 1
    color = max(color, key=color.get)
    for c in range(c0, c1 + 1):
        output[r0][c] = color
        output[r1][c] = color
    for r in range(r0, r1 + 1):
        output[r][c0] = color
        output[r][c1] = color
    return output
