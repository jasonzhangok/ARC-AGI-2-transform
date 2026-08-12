def transform(grid):
    split_r = next(r for r, row in enumerate(grid) if all(v == 4 for v in row))
    split_c = next(c for c in range(len(grid[0])) if all(row[c] == 4 for row in grid))
    quadrants = (
        [row[split_c + 1:] for row in grid[split_r + 1:]],
        [row[:split_c] for row in grid[:split_r]],
        [row[split_c + 1:] for row in grid[:split_r]],
        [row[:split_c] for row in grid[split_r + 1:]],
    )
    h, w = len(quadrants[0]), len(quadrants[0][0])
    out = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            for part in quadrants:
                if part[r][c] != 0:
                    out[r][c] = part[r][c]
                    break
    output = out
    return output
