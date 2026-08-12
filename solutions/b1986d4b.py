def transform(grid):
    height = len(grid)
    width = len(grid[0])

    frequencies = {}
    for row in grid:
        for color in row:
            frequencies[color] = frequencies.get(color, 0) + 1

    background = None
    background_count = -1
    for color in frequencies:
        if frequencies[color] > background_count:
            background = color
            background_count = frequencies[color]

    visited = [[False] * width for _ in range(height)]
    square_info = {}
    for start_row in range(height):
        for start_col in range(width):
            if visited[start_row][start_col]:
                continue
            visited[start_row][start_col] = True
            color = grid[start_row][start_col]
            if color == background:
                continue

            cells = [(start_row, start_col)]
            position = 0
            min_row = start_row
            max_row = start_row
            min_col = start_col
            max_col = start_col
            while position < len(cells):
                row, col = cells[position]
                position += 1
                if row < min_row:
                    min_row = row
                if row > max_row:
                    max_row = row
                if col < min_col:
                    min_col = col
                if col > max_col:
                    max_col = col
                for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = row + delta_row
                    next_col = col + delta_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and not visited[next_row][next_col]
                            and grid[next_row][next_col] == color):
                        visited[next_row][next_col] = True
                        cells.append((next_row, next_col))

            side = max_row - min_row + 1
            if side >= 2 and max_col - min_col + 1 == side and len(cells) == side * side:
                key = (side, color)
                square_info[key] = square_info.get(key, 0) + 1

    squares = []
    for side, color in square_info:
        squares.append((side, color, square_info[(side, color)]))
    squares.sort()

    group_count = squares[0][2] - 1
    for side, color, count in squares[1:]:
        if count > group_count:
            group_count = count

    output_height = squares[-1][0] + 1
    result = [[] for _ in range(output_height)]
    for group in range(group_count):
        group_side = 0
        for side, color, count in squares:
            if group < count and side > group_side:
                group_side = side

        tile = [[background] * group_side for _ in range(group_side)]
        for side, color, count in squares[::-1]:
            if group < count:
                for row in range(side):
                    for col in range(side):
                        tile[row][col] = color

        for row in range(output_height):
            if row < group_side:
                result[row].extend(tile[row])
            else:
                result[row].extend([background] * group_side)
            result[row].append(background)

    return result
