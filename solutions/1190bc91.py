def transform(grid):
    height = len(grid)
    width = len(grid[0])

    best = None
    for row in range(height):
        col = 0
        while col < width:
            if grid[row][col] == 0:
                col += 1
                continue
            start = col
            while col < width and grid[row][col] != 0:
                col += 1
            colors = grid[row][start:col]
            if len(colors) >= 3 and len(set(colors)) >= 2:
                if best is None or len(colors) > best[0]:
                    best = (len(colors), False, row, start, colors)

    for col in range(width):
        row = 0
        while row < height:
            if grid[row][col] == 0:
                row += 1
                continue
            start = row
            colors = []
            while row < height and grid[row][col] != 0:
                colors.append(grid[row][col])
                row += 1
            if len(colors) >= 3 and len(set(colors)) >= 2:
                if best is None or len(colors) > best[0]:
                    best = (len(colors), True, start, col, colors)

    length, vertical, line_row, line_col, colors = best
    output = [[0 for _ in range(width)] for _ in range(height)]

    if not vertical:
        for row in range(height):
            distance = abs(row - line_row)
            for index in range(min(2, length)):
                col = line_col - distance + index
                if 0 <= col < width:
                    output[row][col] = colors[index]
            for index in range(max(0, length - distance)):
                col = line_col + distance + index
                if 0 <= col < width:
                    output[row][col] = colors[index]
    else:
        for col in range(width):
            distance = abs(col - line_col)
            for index in range(min(2, length)):
                row = line_row - distance + index
                if 0 <= row < height:
                    output[row][col] = colors[index]
            for index in range(max(0, length - distance)):
                row = line_row + distance + index
                if 0 <= row < height:
                    output[row][col] = colors[index]

    if vertical:
        line_cells = {(line_row + index, line_col) for index in range(length)}
    else:
        line_cells = {(line_row, line_col + index) for index in range(length)}

    grouped = set()
    for seed_row in range(height):
        for seed_col in range(width):
            if (grid[seed_row][seed_col] == 0 or
                    (seed_row, seed_col) in line_cells or
                    (seed_row, seed_col) in grouped):
                continue

            color = grid[seed_row][seed_col]
            component = [(seed_row, seed_col)]
            grouped.add((seed_row, seed_col))
            cursor = 0
            while cursor < len(component):
                row, col = component[cursor]
                cursor += 1
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_step
                    next_col = col + col_step
                    if (0 <= next_row < height and 0 <= next_col < width and
                            (next_row, next_col) not in grouped and
                            (next_row, next_col) not in line_cells and
                            grid[next_row][next_col] == color):
                        grouped.add((next_row, next_col))
                        component.append((next_row, next_col))

            region = []
            visited = set()
            for row, col in component:
                if output[row][col] == 0:
                    output[row][col] = color
                    region.append((row, col))
                    visited.add((row, col))

            cursor = 0
            while cursor < len(region):
                row, col = region[cursor]
                cursor += 1
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_step
                    next_col = col + col_step
                    if (0 <= next_row < height and 0 <= next_col < width and
                            output[next_row][next_col] == 0 and
                            (next_row, next_col) not in visited):
                        output[next_row][next_col] = color
                        visited.add((next_row, next_col))
                        region.append((next_row, next_col))

    return output
