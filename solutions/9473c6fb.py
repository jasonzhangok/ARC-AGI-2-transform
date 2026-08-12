def transform(grid):
    output = [row[:] for row in grid]
    points = []
    occupied_rows = []
    occupied_cols = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != 7:
                points.append((row, col))
                if row not in occupied_rows:
                    occupied_rows.append(row)
                if col not in occupied_cols:
                    occupied_cols.append(col)
    if len(occupied_rows) >= len(occupied_cols):
        points.sort()
    else:
        column_first = []
        for row, col in points:
            column_first.append((col, row))
        column_first.sort()
        points = []
        for col, row in column_first:
            points.append((row, col))
    cycle = (2, 8, 5)
    for index in range(len(points)):
        row, col = points[index]
        output[row][col] = cycle[index % 3]
    return output
