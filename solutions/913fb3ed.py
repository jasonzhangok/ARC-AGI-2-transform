NEIGHBOR_COLOR = {3: 6, 8: 4, 2: 1}


def transform(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    centers = [(r, c, value) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    for r, c, value in centers:
        surround = NEIGHBOR_COLOR[value]
        for x in range(max(0, r - 1), min(h, r + 2)):
            for y in range(max(0, c - 1), min(w, c + 2)):
                if grid[x][y] == 0:
                    output[x][y] = surround
    for r, c, value in centers:
        output[r][c] = value
    return output
