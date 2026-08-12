def transform(grid):
    height = len(grid)
    width = len(grid[0])
    points = []
    colors = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                points.append((row, col, grid[row][col]))
                if grid[row][col] not in colors:
                    colors.append(grid[row][col])

    output = [row[:] for row in grid]
    for row, col, color in points:
        other = colors[1] if color == colors[0] else colors[0]
        for target_row in range(row - 1, row + 2):
            for target_col in range(col - 1, col + 2):
                if 0 <= target_row < height and 0 <= target_col < width:
                    output[target_row][target_col] = other
        output[row][col] = color

    rows = sorted(set(row for row, col, color in points))
    cols = sorted(set(col for row, col, color in points))
    for row in rows:
        start = cols[0] + 2
        end = cols[-1] - 2
        for col in range(start, end + 1):
            if min(col - start, end - col) % 2 == 0:
                output[row][col] = 5
    for col in cols:
        start = rows[0] + 2
        end = rows[-1] - 2
        for row in range(start, end + 1):
            if min(row - start, end - row) % 2 == 0:
                output[row][col] = 5
    return output
