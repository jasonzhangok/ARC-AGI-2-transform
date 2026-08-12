from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    colors = [value for row in grid for value in row if value != 0]
    counts = Counter(colors)
    best = None
    for base in counts:
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == base]
        r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
        c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
        border = (2 * (r1 - r0 + 1) + 2 * (c1 - c0 + 1) - 4)
        score = counts[base] / border if border else 0
        if best is None or score > best[0]:
            best = (score, base, r0, r1, c0, c1)
    _, base, r0, r1, c0, c1 = best
    line_color = next(color for color in counts if color != base)
    output = [[0 if value == line_color else value for value in row] for row in grid]
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            output[r][c] = base if r in (r0, r1) or c in (c0, c1) else 0
    for c in range(w):
        if c < c0 or c > c1:
            output[r0][c] = line_color
    for r in range(h):
        if r < r0 or r > r1:
            output[r][c1] = line_color
    return output
