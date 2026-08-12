def transform(grid):
    output = [row[:] for row in grid]
    key_points = [
        (r, c)
        for r in range(2)
        for c in range(2)
        if grid[r][c] != 0
    ]
    mapping = {}
    for r in range(2):
        left, right = grid[r][0], grid[r][1]
        mapping[left] = right
        mapping[right] = left

    key_set = set(key_points)
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0 and (r, c) not in key_set:
                output[r][c] = mapping[value]
    return output
