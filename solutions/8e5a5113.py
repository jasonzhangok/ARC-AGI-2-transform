def rotate_clockwise(grid):
    return [list(row) for row in zip(*grid[::-1])]


def transform(grid):
    pattern = [row[:3] for row in grid]
    quarter = rotate_clockwise(pattern)
    half = rotate_clockwise(quarter)
    return [pattern[r] + [5] + quarter[r] + [5] + half[r] for r in range(3)]
