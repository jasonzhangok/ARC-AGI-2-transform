def transform(grid):
    height, width = (len(grid), len(grid[0]))
    result = [row[:] for row in grid]
    counts = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        counts[cell_value] = counts.get(cell_value, 0) + 1
    marker = min((color for color in counts if color != 5), key=counts.get)
    fives = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5]
    top, bottom = (min((r for r, _ in fives)), max((r for r, _ in fives)))
    left, right = (min((c for _, c in fives)), max((c for _, c in fives)))
    markers = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == marker]
    for r, c in markers:
        result[r][c] = 0
    for r in range(top, bottom + 1):
        left_count = sum((mr == r and mc < left for mr, mc in markers))
        right_count = sum((mr == r and mc > right for mr, mc in markers))
        for distance in range(1, left_count + 1):
            result[r][left - distance] = 5
        for distance in range(1, right_count + 1):
            result[r][right + distance] = 5
    for c in range(left, right + 1):
        top_count = sum((mc == c and mr < top for mr, mc in markers))
        bottom_count = sum((mc == c and mr > bottom for mr, mc in markers))
        for distance in range(1, top_count + 1):
            result[top - distance][c] = 5
        for distance in range(1, bottom_count + 1):
            result[bottom + distance][c] = 5
    output = result
    return output
