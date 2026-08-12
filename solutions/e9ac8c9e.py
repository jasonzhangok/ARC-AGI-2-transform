def transform(grid):
    height = len(grid)
    width = len(grid[0])
    remaining = set((row, column) for row in range(height) for column in range(width)
                    if grid[row][column] == 5)
    blocks = []
    while remaining:
        cells = [remaining.pop()]
        cursor = 0
        while cursor < len(cells):
            row, column = cells[cursor]
            cursor += 1
            for neighbor in ((row - 1, column), (row + 1, column),
                             (row, column - 1), (row, column + 1)):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    cells.append(neighbor)
        blocks.append(cells)

    output = [[0 for column in range(width)] for row in range(height)]
    markers = [(row, column, grid[row][column])
               for row in range(height) for column in range(width)
               if grid[row][column] not in (0, 5)]
    for cells in blocks:
        top = min(row for row, column in cells)
        bottom = max(row for row, column in cells)
        left = min(column for row, column in cells)
        right = max(column for row, column in cells)
        middle_row = (top + bottom + 1) // 2
        middle_column = (left + right + 1) // 2
        colors = {}
        for row, column, color in markers:
            quadrant = (0 if row < middle_row else 1,
                        0 if column < middle_column else 1)
            distance = min(abs(row - cell_row) + abs(column - cell_column)
                           for cell_row, cell_column in cells)
            if quadrant not in colors or distance < colors[quadrant][0]:
                colors[quadrant] = (distance, color)
        for row, column in cells:
            quadrant = (0 if row < middle_row else 1,
                        0 if column < middle_column else 1)
            output[row][column] = colors[quadrant][1]
    return output
