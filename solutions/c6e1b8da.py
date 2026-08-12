def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = []
    for row in grid:
        for value in row:
            if value != 0 and value not in colors:
                colors.append(value)

    objects = []
    for color in colors:
        cells = []
        for r in range(height):
            for c in range(width):
                if grid[r][c] == color:
                    cells.append((r, c))

        top = min(r for r, c in cells)
        bottom = max(r for r, c in cells)
        left = min(c for r, c in cells)
        right = max(c for r, c in cells)
        source_top = top
        source_bottom = bottom
        source_left = left
        source_right = right
        shift_r = 0
        shift_c = 0
        moving = False

        row_intervals = []
        rows_are_solid = True
        for r in range(top, bottom + 1):
            occupied = []
            for c in range(width):
                if grid[r][c] == color:
                    occupied.append(c)
            if not occupied or len(occupied) != occupied[-1] - occupied[0] + 1:
                rows_are_solid = False
                break
            row_intervals.append((occupied[0], occupied[-1]))

        if rows_are_solid and len(row_intervals) >= 3:
            for special in range(1, len(row_intervals) - 1):
                ordinary = []
                for index in range(len(row_intervals)):
                    if index != special:
                        ordinary.append(row_intervals[index])
                base = ordinary[0]
                all_equal = True
                for interval in ordinary:
                    if interval != base:
                        all_equal = False
                extension = row_intervals[special]
                if all_equal and base[1] - base[0] + 1 >= 2:
                    if extension[0] < base[0] and extension[1] == base[1]:
                        source_left = base[0]
                        source_right = base[1]
                        shift_c = extension[0] - base[0]
                        moving = True
                        break
                    if extension[0] == base[0] and extension[1] > base[1]:
                        source_left = base[0]
                        source_right = base[1]
                        shift_c = extension[1] - base[1]
                        moving = True
                        break

        if not moving:
            column_intervals = []
            columns_are_solid = True
            for c in range(left, right + 1):
                occupied = []
                for r in range(height):
                    if grid[r][c] == color:
                        occupied.append(r)
                if not occupied or len(occupied) != occupied[-1] - occupied[0] + 1:
                    columns_are_solid = False
                    break
                column_intervals.append((occupied[0], occupied[-1]))

            if columns_are_solid and len(column_intervals) >= 3:
                for special in range(1, len(column_intervals) - 1):
                    ordinary = []
                    for index in range(len(column_intervals)):
                        if index != special:
                            ordinary.append(column_intervals[index])
                    base = ordinary[0]
                    all_equal = True
                    for interval in ordinary:
                        if interval != base:
                            all_equal = False
                    extension = column_intervals[special]
                    if all_equal and base[1] - base[0] + 1 >= 2:
                        if extension[0] < base[0] and extension[1] == base[1]:
                            source_top = base[0]
                            source_bottom = base[1]
                            shift_r = extension[0] - base[0]
                            moving = True
                            break
                        if extension[0] == base[0] and extension[1] > base[1]:
                            source_top = base[0]
                            source_bottom = base[1]
                            shift_r = extension[1] - base[1]
                            moving = True
                            break

        objects.append((
            color,
            source_top,
            source_bottom,
            source_left,
            source_right,
            shift_r,
            shift_c,
            moving,
        ))

    result = [[0 for c in range(width)] for r in range(height)]
    for obj in objects:
        color, top, bottom, left, right, shift_r, shift_c, moving = obj
        if not moving:
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    result[r][c] = color

    for obj in objects:
        color, top, bottom, left, right, shift_r, shift_c, moving = obj
        if moving:
            for r in range(top + shift_r, bottom + shift_r + 1):
                for c in range(left + shift_c, right + shift_c + 1):
                    result[r][c] = color

    return result
