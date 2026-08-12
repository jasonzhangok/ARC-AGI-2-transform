def transform(grid):
    height, width = len(grid), len(grid[0])
    best = (0, 0, 0, 0, 0)

    for top in range(height):
        valid_cols = [True] * width
        for bottom in range(top, height):
            valid_cols = [
                valid_cols[col] and grid[bottom][col] == 0
                for col in range(width)
            ]
            col = 0
            while col < width:
                if not valid_cols[col]:
                    col += 1
                    continue
                left = col
                while col < width and valid_cols[col]:
                    col += 1
                right = col - 1
                area = (bottom - top + 1) * (right - left + 1)
                best = max(best, (area, top, bottom, left, right))

    _, top, bottom, left, right = best
    output = [row[:] for row in grid]
    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            output[row][col] = 8
    return output
