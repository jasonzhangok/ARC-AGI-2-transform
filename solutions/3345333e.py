from collections import Counter


def transform(grid):
    counts = Counter(value for row in grid for value in row if value != 0)
    main = max(counts, key=counts.get)
    occluder = next(color for color in counts if color != main)
    cells = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == main}
    left = min(c for _, c in cells)
    right = max(c for _, c in cells)
    doubled_axis = left + right
    result = [[0 if value == occluder else value for value in row] for row in grid]
    for r, c in cells:
        result[r][doubled_axis - c] = main
    return result
