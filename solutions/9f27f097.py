from collections import Counter, deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
    zero = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 0]
    zr0, zr1 = min(r for r, _ in zero), max(r for r, _ in zero)
    zc0, zc1 = min(c for _, c in zero), max(c for _, c in zero)
    colors = [v for row in grid for v in row if v not in (bg, 0)]
    ink = Counter(colors).most_common(1)[0][0]
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != bg and grid[r][c] != 0]
    sr0, sr1 = min(r for r, _ in cells), max(r for r, _ in cells)
    sc0, sc1 = min(c for _, c in cells), max(c for _, c in cells)
    out = [row[:] for row in grid]
    for i in range(zr1 - zr0 + 1):
        for j in range(zc1 - zc0 + 1):
            out[zr0 + i][zc0 + j] = grid[sr0 + i][sc1 - j]
    return out
