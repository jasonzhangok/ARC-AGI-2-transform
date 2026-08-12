def transform(grid):
    height = len(grid)
    width = len(grid[0])
    separator_rows = set()
    separator_cols = set()
    for row in range(height):
        if all(grid[row][col] == 8 for col in range(width)):
            separator_rows.add(row)
    for col in range(width):
        if all(grid[row][col] == 8 for row in range(height)):
            separator_cols.add(col)

    row_cell = []
    cell = 0
    for row in range(height):
        if row in separator_rows:
            row_cell.append(-1)
            cell += 1
        else:
            row_cell.append(cell)
    col_cell = []
    cell = 0
    for col in range(width):
        if col in separator_cols:
            col_cell.append(-1)
            cell += 1
        else:
            col_cell.append(cell)

    markers = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color != 0 and color != 8:
                if color not in markers:
                    markers[color] = set()
                markers[color].add((row_cell[row], col_cell[col]))

    painted = {}
    for color in markers:
        points = list(markers[color])
        for first in range(len(points)):
            for second in range(first + 1, len(points)):
                row1, col1 = points[first]
                row2, col2 = points[second]
                if row1 == row2:
                    left = min(col1, col2)
                    right = max(col1, col2)
                    for col in range(left, right + 1):
                        point = (row1, col)
                        if point not in painted:
                            painted[point] = set()
                        painted[point].add(color)
                if col1 == col2:
                    top = min(row1, row2)
                    bottom = max(row1, row2)
                    for row in range(top, bottom + 1):
                        point = (row, col1)
                        if point not in painted:
                            painted[point] = set()
                        painted[point].add(color)

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            point = (row_cell[row], col_cell[col])
            if point in painted:
                colors = painted[point]
                if len(colors) == 1:
                    output[row][col] = next(iter(colors))
                else:
                    output[row][col] = 6
    return output
