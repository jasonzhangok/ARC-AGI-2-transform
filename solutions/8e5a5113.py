def transform(grid):
    pattern = [row[:3] for row in grid]
    _grid = pattern
    rotate_clockwise_result_1 = [list(row) for row in zip(*_grid[::-1])]
    quarter = rotate_clockwise_result_1
    _grid = quarter
    rotate_clockwise_result_2 = [list(row) for row in zip(*_grid[::-1])]
    half = rotate_clockwise_result_2
    output = [pattern[r] + [5] + quarter[r] + [5] + half[r] for r in range(3)]
    return output
