from collections import Counter


def largest_solid_rectangle(grid, color):
    h, w = len(grid), len(grid[0])
    best = (0, 0, 0, 0, 0)
    for r0 in range(h):
        for c0 in range(w):
            if grid[r0][c0] != color:
                continue
            for r1 in range(r0, h):
                for c1 in range(c0, w):
                    area = (r1 - r0 + 1) * (c1 - c0 + 1)
                    if area > best[0] and all(grid[r][c] == color for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)):
                        best = (area, r0, r1, c0, c1)
    return best


def transform(grid):
    h, w = len(grid), len(grid[0])
    colors = [value for value in Counter(value for row in grid for value in row) if value != 0]
    boxes = {color: largest_solid_rectangle(grid, color) for color in colors}
    anchor = next(color for color in colors if boxes[color][0] == sum(row.count(color) for row in grid))
    moving = next(color for color in colors if color != anchor)
    _, ar0, ar1, ac0, ac1 = boxes[anchor]
    _, mr0, mr1, mc0, mc1 = boxes[moving]
    output = [[0 if value == moving else value for value in row] for row in grid]
    dr = (mr0 + mr1) - (ar0 + ar1)
    dc = (mc0 + mc1) - (ac0 + ac1)
    if abs(dc) > abs(dr):
        shift = (ac0 - 1 - mc1) if dc < 0 else (ac1 + 1 - mc0)
        nr0, nc0 = mr0, mc0 + shift
    else:
        shift = (ar0 - 1 - mr1) if dr < 0 else (ar1 + 1 - mr0)
        nr0, nc0 = mr0 + shift, mc0
    for r in range(mr1 - mr0 + 1):
        for c in range(mc1 - mc0 + 1):
            output[nr0 + r][nc0 + c] = moving
    return output
