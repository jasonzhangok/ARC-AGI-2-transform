def transform(grid):
    h, w = len(grid), len(grid[0])
    frame = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    r0, r1 = min(r for r, _ in frame), max(r for r, _ in frame)
    c0, c1 = min(c for _, c in frame), max(c for _, c in frame)
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    out = [[0 if value == 5 else value for value in row] for row in grid]
    vertical_strength = sum(grid[r][c0] == 2 for r in range(r0, r1 + 1)) + sum(
        grid[r][c1] == 2 for r in range(r0, r1 + 1))
    horizontal_strength = sum(grid[r0][c] == 2 for c in range(c0, c1 + 1)) + sum(
        grid[r1][c] == 2 for c in range(c0, c1 + 1))
    for r, c in fives:
        nr, nc = r, c
        if vertical_strength > horizontal_strength:
            if c - c0 <= c1 - c:
                nc = 2 * c0 - c
            else:
                nc = 2 * c1 - c
        else:
            if r - r0 <= r1 - r:
                nr = 2 * r0 - r
            else:
                nr = 2 * r1 - r
        out[nr][nc] = 5
    output = out
    return output
