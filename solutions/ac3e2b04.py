def transform(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    templates = []
    for top in range(h - 2):
        for left in range(w - 2):
            if (grid[top + 1][left + 1] == 2
                    and all(grid[top + r][left + c] == 3
                            for r in range(3) for c in range(3)
                            if (r, c) != (1, 1))):
                templates.append((top + 1, left + 1))
    template_centers = set(templates)

    vertical_lines = [c for c in range(w)
                      if sum(grid[r][c] == 2 for r in range(h)) >= 3]
    horizontal_lines = [r for r in range(h)
                        if sum(grid[r][c] == 2 for c in range(w)) >= 3]

    for center_r, center_c in templates:
        column_twos = sum(grid[r][center_c] == 2 for r in range(h))
        row_twos = sum(grid[center_r][c] == 2 for c in range(w))
        if column_twos > row_twos:
            for c in range(w):
                if out[center_r][c] == 0:
                    out[center_r][c] = 1
            crossings = [(center_r, c) for c in vertical_lines]
        else:
            for r in range(h):
                if out[r][center_c] == 0:
                    out[r][center_c] = 1
            crossings = [(r, center_c) for r in horizontal_lines]

        for cross_r, cross_c in crossings:
            if (cross_r, cross_c) in template_centers:
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = cross_r + dr, cross_c + dc
                    if 0 <= nr < h and 0 <= nc < w:
                        out[nr][nc] = 2 if (dr, dc) == (0, 0) else 1
    return out
