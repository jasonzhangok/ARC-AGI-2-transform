def transform(grid):
    h, w = len(grid), len(grid[0])
    background = 7
    output = [[background] * w for _ in range(h)]
    for r in (0, h - 1):
        for c in (0, w - 1):
            color = grid[r][c]
            if color == background:
                continue
            left = c == 0
            if r == 0:
                cols = (1, 2) if left else (w - 3, w - 2)
                for y in (1, 2):
                    for x in cols:
                        output[y][x] = color
            else:
                x = 2 if left else w - 3
                output[h - 4][x] = color
                output[h - 3][x] = color
                output[h - 2][x + (1 if left else -1)] = color
    return output
