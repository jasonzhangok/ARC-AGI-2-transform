def transform(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    rare = {v for v, n in counts.items() if n <= 3}
    by_key = {}
    for r in range(h):
        for c in range(w):
            if grid[r][c] in rare:
                by_key.setdefault((grid[r][c], r % 5, c % 5), []).append((r // 5, c // 5))
    for (color, lr, lc), blocks in by_key.items():
        for br in {x for x, _ in blocks}:
            cols = [y for x, y in blocks if x == br]
            if len(cols) >= 2:
                for bc in range(min(cols), max(cols) + 1): out[br * 5 + lr][bc * 5 + lc] = color
        for bc in {y for _, y in blocks}:
            rows = [x for x, y in blocks if y == bc]
            if len(rows) >= 2:
                for br in range(min(rows), max(rows) + 1): out[br * 5 + lr][bc * 5 + lc] = color
    output = out
    return output
