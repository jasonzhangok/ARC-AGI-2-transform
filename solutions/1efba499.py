

def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    main_color = {}
    for cell_value in (value for row in grid for value in row if value != 0):
        main_color[cell_value] = main_color.get(cell_value, 0) + 1
    main_color = max(main_color, key=main_color.get)
    main = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == main_color
    }
    moves = []

    for row in range(height):
        occupied = sorted(col for r, col in main if r == row)
        if not occupied:
            continue
        left_edge, right_edge = occupied[0], occupied[-1]
        left = [
            col for col in range(left_edge)
            if grid[row][col] not in (0, main_color)
        ]
        right = [
            col for col in range(right_edge + 1, width)
            if grid[row][col] not in (0, main_color)
        ]
        if left and right:
            left_source, right_source = max(left), min(right)
            if grid[row][left_source] != grid[row][right_source]:
                moves.append(((row, left_source), (row, right_edge + 1)))
                moves.append(((row, right_source), (row, left_edge - 1)))

    for col in range(width):
        occupied = sorted(row for row, c in main if c == col)
        if not occupied:
            continue
        top_edge, bottom_edge = occupied[0], occupied[-1]
        above = [
            row for row in range(top_edge)
            if grid[row][col] not in (0, main_color)
        ]
        below = [
            row for row in range(bottom_edge + 1, height)
            if grid[row][col] not in (0, main_color)
        ]
        if above and below:
            top_source, bottom_source = max(above), min(below)
            if grid[top_source][col] != grid[bottom_source][col]:
                moves.append(((top_source, col), (bottom_edge + 1, col)))
                moves.append(((bottom_source, col), (top_edge - 1, col)))

    for source, _ in moves:
        output[source[0]][source[1]] = 0
    for source, target in moves:
        output[target[0]][target[1]] = grid[source[0]][source[1]]
    return output
