def transform(grid):
    h, w = len(grid), len(grid[0])
    start = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 2)
    target = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 1)
    r, c = start
    output = [row[:] for row in grid]
    dr, dc = target[0] - r, target[1] - c
    if dr and dc:
        _value = dr
        sign_result_1 = (_value > 0) - (_value < 0)
        r += sign_result_1
        _value = dc
        sign_result_2 = (_value > 0) - (_value < 0)
        c += sign_result_2
        if (r, c) != target:
            output[r][c] = 3
    while abs(target[0] - r) != abs(target[1] - c):
        if abs(target[0] - r) > abs(target[1] - c):
            _value = target[0] - r
            sign_result_3 = (_value > 0) - (_value < 0)
            r += sign_result_3
        else:
            _value = target[1] - c
            sign_result_4 = (_value > 0) - (_value < 0)
            c += sign_result_4
        if (r, c) != target:
            output[r][c] = 3
    while (r, c) != target:
        _value = target[0] - r
        sign_result_5 = (_value > 0) - (_value < 0)
        r += sign_result_5
        _value = target[1] - c
        sign_result_6 = (_value > 0) - (_value < 0)
        c += sign_result_6
        if (r, c) != target:
            output[r][c] = 3
    return output
