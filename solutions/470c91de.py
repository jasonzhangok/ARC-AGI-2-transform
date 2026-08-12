from collections import Counter


def transform(grid):
    h, w = len(grid), len(grid[0])
    background = Counter(v for row in grid for v in row).most_common(1)[0][0]
    colors = sorted({v for row in grid for v in row if v not in (background, 8)})
    eights = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    objects = []
    used = set()
    for color in colors:
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        for er, ec in eights:
            if (er, ec) in used:
                continue
            all_cells = cells + [(er, ec)]
            r0, r1 = min(r for r, _ in all_cells), max(r for r, _ in all_cells)
            c0, c1 = min(c for _, c in all_cells), max(c for _, c in all_cells)
            if len(all_cells) != (r1 - r0 + 1) * (c1 - c0 + 1):
                continue
            if all(grid[r][c] in (color, 8)
                   for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)):
                dr = -1 if er == r0 else 1
                dc = -1 if ec == c0 else 1
                objects.append((color, r0, r1, c0, c1, dr, dc))
                used.add((er, ec))
                break
    out = [[background] * w for _ in range(h)]
    for color, r0, r1, c0, c1, dr, dc in objects:
        for r in range(r0 + dr, r1 + dr + 1):
            for c in range(c0 + dc, c1 + dc + 1):
                if 0 <= r < h and 0 <= c < w:
                    out[r][c] = color
    return out
