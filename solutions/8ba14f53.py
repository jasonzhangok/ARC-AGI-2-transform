def transform(grid):
    colors = []
    for row in grid:
        for value in row:
            if value != 0 and value not in colors:
                colors.append(value)
    result = [[0, 0, 0] for _ in range(3)]
    output_row = 0
    for color in colors:
        _grid = grid
        _color = color
        height = len(_grid)
        width = len(_grid[0])
        reachable = set()
        queue = []
        for row in range(height):
            for col in (0, width - 1):
                if _grid[row][col] != _color and (row, col) not in reachable:
                    reachable.add((row, col))
                    queue.append((row, col))
        for col in range(width):
            for row in (0, height - 1):
                if _grid[row][col] != _color and (row, col) not in reachable:
                    reachable.add((row, col))
                    queue.append((row, col))
        while queue:
            row, col = queue.pop(0)
            for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= next_row < height and 0 <= next_col < width and (_grid[next_row][next_col] != _color) and ((next_row, next_col) not in reachable):
                    reachable.add((next_row, next_col))
                    queue.append((next_row, next_col))
        _enclosed_zero_count_result_1 = sum((_grid[row][col] == 0 and (row, col) not in reachable for row in range(height) for col in range(width)))
        enclosed_count = _enclosed_zero_count_result_1
        for index in range(enclosed_count):
            result[output_row + index // 3][index % 3] = color
        output_row += (enclosed_count + 2) // 3
    output = result
    return output
