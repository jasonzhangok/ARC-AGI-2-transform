from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    frame = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    r0, r1 = min(r for r, _ in frame), max(r for r, _ in frame)
    c0, c1 = min(c for _, c in frame), max(c for _, c in frame)
    markers = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0, 5)]
    center_r, center_c = (r0 + r1) / 2, (c0 + c1) / 2
    diagonal = {}
    for r, c, color in markers:
        diagonal[(r < center_r) == (c < center_c)] = color
    output = [row[:] for row in grid]
    mid_r, mid_c = (r0 + r1) // 2, (c0 + c1) // 2
    for r in range(r0 + 1, r1):
        for c in range(c0 + 1, c1):
            parity = (r <= mid_r) == (c <= mid_c)
            output[r][c] = diagonal[parity]
    return output
