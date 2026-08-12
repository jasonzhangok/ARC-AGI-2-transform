def transform(grid):
    h, w = len(grid), len(grid[0])
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    r0, r1 = min(r for r, _ in ones), max(r for r, _ in ones)
    c0, c1 = min(c for _, c in ones), max(c for _, c in ones)
    tokens = [grid[i][i] for i in range(min(r0, c0)) if grid[i][i] != 0]
    output = [row[:] for row in grid]
    for r in range(r0 + 1, r1):
        for c in range(c0 + 1, c1):
            depth = min(r - r0 - 1, r1 - r - 1, c - c0 - 1, c1 - c - 1)
            output[r][c] = tokens[min(depth, len(tokens) - 1)]
    return output
