def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seeds = [
        (row, col, grid[row][col])
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0
    ]

    paths = []
    endpoints = []
    for row, col, color in seeds:
        if color == 6:
            endpoint = (row - 6, col)
            path = [(r, col) for r in range(row - 5, row)]
        elif color == 3:
            endpoint = (row + 3, col)
            path = [(r, col) for r in range(row + 1, row + 3)]
        elif color == 2:
            endpoint = (row, col - 4)
            path = [(row, c) for c in range(col - 3, col)]
        else:
            endpoint = (row - 1, col + 2)
            path = [(row, col + 1), (row, col + 2)]
        paths.append(set(path))
        endpoints.append((endpoint, color))

    output = [row[:] for row in grid]
    for path in paths:
        for row, col in path:
            output[row][col] = 5
    for (row, col), color in endpoints:
        output[row][col] = color

    intersections = {
        cell
        for i, path in enumerate(paths)
        for cell in path
        if sum(cell in other for other in paths[i + 1:]) > 0
    }
    for row, col in intersections:
        output[row][col] = 4
        row += 1
        col -= 1
        while row < height and col >= 0:
            if output[row][col] == 0:
                output[row][col] = 4
            row += 1
            col -= 1

    return output
