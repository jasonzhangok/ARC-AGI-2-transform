def transform(grid):
    h, w = len(grid), len(grid[0])
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    fours = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    out = [row[:] for row in grid]
    for r, c in fours:
        distance = min(max(abs(r - y), abs(c - x)) for y, x in fives)
        radius = distance - 1
        for y in range(max(0, r - radius), min(h, r + radius + 1)):
            for x in range(max(0, c - radius), min(w, c + radius + 1)):
                if out[y][x] == 0:
                    out[y][x] = 2
    return out
