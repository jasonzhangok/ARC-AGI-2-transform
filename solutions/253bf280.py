def transform(grid):
    output = [row[:] for row in grid]
    points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 8]
    for i, (row1, col1) in enumerate(points):
        for row2, col2 in points[i + 1:]:
            if row1 == row2:
                for col in range(min(col1, col2) + 1, max(col1, col2)):
                    output[row1][col] = 3
            elif col1 == col2:
                for row in range(min(row1, row2) + 1, max(row1, row2)):
                    output[row][col1] = 3
    return output
