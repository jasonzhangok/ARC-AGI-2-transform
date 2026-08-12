def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    marker_colors = sorted({value for row in grid for value in row
                            if value not in (0, 8)})

    separator_rows = [r for r in range(h)
                      if all(value != 8 for value in grid[r])]
    separator_cols = [c for c in range(w)
                      if all(grid[r][c] != 8 for r in range(h))]

    def nearest(value, candidates):
        return min(candidates, key=lambda candidate: abs(candidate - value))

    for color in marker_colors:
        markers = [(r, c) for r in range(h) for c in range(w)
                   if grid[r][c] == color]
        corners = [(nearest(r, separator_rows), nearest(c, separator_cols))
                   for r, c in markers]
        top, bottom = sorted([corners[0][0], corners[1][0]])
        left, right = sorted([corners[0][1], corners[1][1]])

        for c in range(left, right + 1):
            if out[top][c] == 0:
                out[top][c] = color
            if out[bottom][c] == 0:
                out[bottom][c] = color
        for r in range(top, bottom + 1):
            if out[r][left] == 0:
                out[r][left] = color
            if out[r][right] == 0:
                out[r][right] = color

        for r in range(top + 1, bottom):
            for c in range(left + 1, right):
                if (grid[r][c] == 0 and grid[r - 1][c] == 8
                        and grid[r + 1][c] == 8
                        and grid[r][c - 1] == 8
                        and grid[r][c + 1] == 8):
                    out[r][c] = color
    return out
