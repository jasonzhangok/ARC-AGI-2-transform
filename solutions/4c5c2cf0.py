from collections import Counter


def transform(grid):
    counts = Counter(v for row in grid for v in row if v != 0)
    marker_color = min(counts, key=lambda v: counts[v])
    marker = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row)
              if v == marker_color]
    center_r = (min(r for r, _ in marker) + max(r for r, _ in marker)) // 2
    center_c = (min(c for _, c in marker) + max(c for _, c in marker)) // 2
    pattern_color = next(v for v in counts if v != marker_color)
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    for r in range(h):
        for c in range(w):
            if grid[r][c] != pattern_color:
                continue
            for y, x in ((r, c), (2 * center_r - r, c),
                         (r, 2 * center_c - c),
                         (2 * center_r - r, 2 * center_c - c)):
                if 0 <= y < h and 0 <= x < w:
                    out[y][x] = pattern_color
    return out
