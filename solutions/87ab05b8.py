

def transform(grid):
    h, w = len(grid), len(grid[0])
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    red = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    r, c = red[0]
    r0, c0 = (r // 2) * 2, (c // 2) * 2
    output = [[background] * w for _ in range(h)]
    for x in range(r0, min(r0 + 2, h)):
        for y in range(c0, min(c0 + 2, w)):
            output[x][y] = 2
    return output
