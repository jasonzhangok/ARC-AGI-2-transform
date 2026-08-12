def transform(grid):
    height = len(grid)
    width = len(grid[0])
    walls = set()

    for row in range(height):
        column = 0
        while column < width:
            if grid[row][column] == 0:
                column += 1
                continue
            start = column
            while column < width and grid[row][column] != 0:
                column += 1
            if column - start >= 5:
                for wall_column in range(start, column):
                    walls.add((row, wall_column))

    for column in range(width):
        row = 0
        while row < height:
            if grid[row][column] == 0:
                row += 1
                continue
            start = row
            while row < height and grid[row][column] != 0:
                row += 1
            if row - start >= 5:
                for wall_row in range(start, row):
                    walls.add((wall_row, column))

    output = [row[:] for row in grid]
    seen = set()
    for start_row in range(height):
        for start_column in range(width):
            if ((start_row, start_column) in walls
                    or (start_row, start_column) in seen):
                continue
            stack = [(start_row, start_column)]
            seen.add((start_row, start_column))
            region = []
            while stack:
                row, column = stack.pop()
                region.append((row, column))
                for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_step
                    next_column = column + column_step
                    if (0 <= next_row < height and 0 <= next_column < width
                            and (next_row, next_column) not in walls
                            and (next_row, next_column) not in seen):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))

            boundary_markers = set()
            for row, column in region:
                for row_step in (-1, 0, 1):
                    for column_step in (-1, 0, 1):
                        neighbor = (row + row_step, column + column_step)
                        if neighbor in walls:
                            value = grid[neighbor[0]][neighbor[1]]
                            if value not in (0, 1):
                                boundary_markers.add(neighbor)

            color_counts = {}
            for row, column in boundary_markers:
                color = grid[row][column]
                color_counts[color] = color_counts.get(color, 0) + 1
            if not color_counts:
                continue
            largest_count = max(color_counts.values())
            region_color = min(color for color in color_counts
                               if color_counts[color] == largest_count)
            for row, column in region:
                if grid[row][column] == 1:
                    output[row][column] = region_color
    return output
