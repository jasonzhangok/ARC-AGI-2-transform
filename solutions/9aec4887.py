def transform(grid):
    h, w = len(grid), len(grid[0])
    segment_colors = sorted({value for row in grid for value in row
                             if value not in (0, 8)})
    horizontal = []
    vertical = []
    for color in segment_colors:
        cells = [(r, c) for r in range(h) for c in range(w)
                 if grid[r][c] == color]
        rows = {r for r, _ in cells}
        cols = {c for _, c in cells}
        if len(rows) == 1:
            horizontal.append((next(iter(rows)), color, len(cells)))
        elif len(cols) == 1:
            vertical.append((next(iter(cols)), color, len(cells)))

    horizontal.sort()
    vertical.sort()
    top_color = horizontal[0][1]
    bottom_color = horizontal[-1][1]
    left_color = vertical[0][1]
    right_color = vertical[-1][1]
    size = horizontal[0][2]

    mask_cells = [(r, c) for r in range(h) for c in range(w)
                  if grid[r][c] == 8]
    mask_top = min(r for r, _ in mask_cells)
    mask_left = min(c for _, c in mask_cells)
    mask = [[grid[mask_top + r][mask_left + c] == 8
             for c in range(size)] for r in range(size)]

    out_size = size + 2
    out = [[0] * out_size for _ in range(out_size)]
    for index in range(1, size + 1):
        out[0][index] = top_color
        out[-1][index] = bottom_color
        out[index][0] = left_color
        out[index][-1] = right_color

    side_colors = [top_color, bottom_color, left_color, right_color]
    for r in range(size):
        for c in range(size):
            if not mask[r][c]:
                continue
            distances = [r, size - 1 - r, c, size - 1 - c]
            nearest = min(distances)
            closest = [i for i, distance in enumerate(distances)
                       if distance == nearest]
            out[r + 1][c + 1] = (side_colors[closest[0]]
                                  if len(closest) == 1 else 8)
    output = out
    return output
