def transform(grid):
    template = [row[:3] for row in grid[:3]]
    result = [row[:] for row in grid]
    markers = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 1]
    for center_r, center_c in markers:
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                result[center_r + dr][center_c + dc] = template[dr + 1][dc + 1]
    output = result
    return output
