def transform(grid):
    _g = grid
    _cw_result_1 = [list(row) for row in zip(*_g[::-1])]
    cw = _cw_result_1
    _g = cw
    _cw_result_2 = [list(row) for row in zip(*_g[::-1])]
    half = _cw_result_2
    _g = half
    _cw_result_3 = [list(row) for row in zip(*_g[::-1])]
    ccw = _cw_result_3
    output = [grid[r] + ccw[r] for r in range(len(grid))] + [half[r] + cw[r] for r in range(len(grid))]
    return output
