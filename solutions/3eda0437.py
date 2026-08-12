def transform(grid):
    height, width = len(grid), len(grid[0])
    excluded_rows = {
        r for r, row in enumerate(grid) if any(value not in (0, 1) for value in row)
    }
    best = None
    best_area = -1
    for top in range(height):
        for bottom in range(top, height):
            if any(r in excluded_rows for r in range(top, bottom + 1)):
                continue
            for left in range(width):
                for right in range(left, width):
                    area = (bottom - top + 1) * (right - left + 1)
                    if area <= best_area:
                        continue
                    if all(
                        grid[r][c] == 0
                        for r in range(top, bottom + 1)
                        for c in range(left, right + 1)
                    ):
                        best_area = area
                        best = (top, bottom, left, right)
    result = [row[:] for row in grid]
    top, bottom, left, right = best
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            result[r][c] = 6
    output = result
    return output
