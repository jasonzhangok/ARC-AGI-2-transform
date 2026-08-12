from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
    seen = set()
    regions = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            cells = []
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = x + dx, y + dy
                    if 0 <= p[0] < h and 0 <= p[1] < w and p not in seen and grid[p[0]][p[1]] != bg:
                        seen.add(p)
                        stack.append(p)
            r0, r1 = min(x for x, _ in cells), max(x for x, _ in cells)
            c0, c1 = min(y for _, y in cells), max(y for _, y in cells)
            regions.append((r0, r1, c0, c1))
    oh = max(r1 - r0 + 1 for r0, r1, _, _ in regions)
    ow = max(c1 - c0 + 1 for _, _, c0, c1 in regions)
    out = [[0] * ow for _ in range(oh)]
    for r0, r1, c0, c1 in regions:
        for r in range(r0, r1 + 1):
            for c in range(c0, c1 + 1):
                if grid[r][c] not in (0, bg):
                    out[r - r0][c - c0] = grid[r][c]
    return out
