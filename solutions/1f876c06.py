from collections import defaultdict


def _line(r0, c0, r1, c1):
    points = []
    dr = abs(r1 - r0)
    dc = abs(c1 - c0)
    sr = 1 if r0 < r1 else -1
    sc = 1 if c0 < c1 else -1
    error = dr - dc
    while True:
        points.append((r0, c0))
        if r0 == r1 and c0 == c1:
            return points
        twice = 2 * error
        if twice > -dc:
            error -= dc
            r0 += sr
        if twice < dr:
            error += dr
            c0 += sc


def transform(grid):
    positions = defaultdict(list)
    for row, values in enumerate(grid):
        for col, color in enumerate(values):
            if color != 0:
                positions[color].append((row, col))
    output = [row[:] for row in grid]
    for color, endpoints in positions.items():
        if len(endpoints) == 2:
            for row, col in _line(*endpoints[0], *endpoints[1]):
                if output[row][col] == 0:
                    output[row][col] = color
    return output
