def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    legend_columns = []
    for c in range(w):
        colors = {grid[r][c] for r in range(h)} - {0, 8}
        if colors:
            legend_columns.append((c, next(iter(colors))))
    legend_columns.sort()
    legend = [color for _, color in legend_columns]

    for r in range(h):
        for c in range(w):
            if grid[r][c] not in (0, 8):
                out[r][c] = 0

    signatures = []
    for c in range(w):
        rows = tuple(r for r in range(h) if grid[r][c] == 8)
        if rows:
            signatures.append((c, rows))

    rectangles = []
    for c, rows in signatures:
        if rectangles and c == rectangles[-1][1] + 1 and rows == rectangles[-1][2]:
            rectangles[-1] = (rectangles[-1][0], c, rows)
        else:
            rectangles.append((c, c, rows))

    for color, (left, right, rows) in zip(legend, rectangles):
        for r in rows:
            for c in range(left, right + 1):
                out[r][c] = color
    output = out
    return output
