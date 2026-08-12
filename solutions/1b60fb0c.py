def transform(grid):
    height, width = len(grid), len(grid[0])
    ones = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 1}
    candidates = []
    for twice_row in range(2 * height - 1):
        for twice_col in range(2 * width - 1):
            rotated = set()
            valid = True
            for row, col in ones:
                new_row_twice = twice_row - (2 * col - twice_col)
                new_col_twice = twice_col + (2 * row - twice_row)
                if new_row_twice % 2 or new_col_twice % 2:
                    valid = False
                    break
                point = (new_row_twice // 2, new_col_twice // 2)
                if not (0 <= point[0] < height and 0 <= point[1] < width):
                    valid = False
                    break
                rotated.add(point)
            if valid and rotated - ones:
                candidates.append((len(rotated & ones), rotated))
    _, rotated = max(candidates, key=lambda item: item[0])
    output = [row[:] for row in grid]
    for row, col in rotated - ones:
        output[row][col] = 2
    return output
