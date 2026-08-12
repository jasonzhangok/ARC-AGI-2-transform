def transform(grid):
    h, w = len(grid), len(grid[0])
    best = (0, 0, 0, 0, 0, 0)
    for r0 in range(h):
        for c0 in range(w):
            color = grid[r0][c0]
            if color == 0:
                continue
            for r1 in range(r0, h):
                for c1 in range(c0, w):
                    area = (r1 - r0 + 1) * (c1 - c0 + 1)
                    if area <= best[0]:
                        continue
                    if all(grid[r][c] == color for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)):
                        best = (area, r0, r1, c0, c1, color)
    output = [[0] * w for _ in range(h)]
    _, r0, r1, c0, c1, color = best
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            output[r][c] = color
    return output
