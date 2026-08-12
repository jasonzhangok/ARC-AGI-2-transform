def transform(grid):
    positions = {}
    for row, values in enumerate(grid):
        for col, color in enumerate(values):
            if color != 0:
                positions.setdefault(color, []).append((row, col))
    output = [row[:] for row in grid]
    for color, endpoints in positions.items():
        if len(endpoints) == 2:
            r0, c0 = endpoints[0]
            r1, c1 = endpoints[1]
            points = []
            dr = abs(r1 - r0)
            dc = abs(c1 - c0)
            sr = 1 if r0 < r1 else -1
            sc = 1 if c0 < c1 else -1
            error = dr - dc
            finished = False
            while not finished:
                points.append((r0, c0))
                if r0 == r1 and c0 == c1:
                    finished = True
                else:
                    twice = 2 * error
                    if twice > -dc:
                        error -= dc
                        r0 += sr
                    if twice < dr:
                        error += dr
                        c0 += sc
            for row, col in points:
                if output[row][col] == 0:
                    output[row][col] = color
    return output
