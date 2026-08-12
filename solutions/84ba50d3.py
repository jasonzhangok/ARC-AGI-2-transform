def transform(grid):
    height = len(grid)
    width = len(grid[0])
    separator_row = None
    for row in range(height):
        if all((grid[row][column] == 2 for column in range(width))):
            separator_row = row
            break
    if separator_row is None:
        output = [row[:] for row in grid]
    else:
        seen = set()
        components = []
        for row in range(height):
            for column in range(width):
                if grid[row][column] != 1 or (row, column) in seen:
                    continue
                stack = [(row, column)]
                seen.add((row, column))
                cells = []
                while stack:
                    current_row, current_column = stack.pop()
                    cells.append((current_row, current_column))
                    for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = current_row + row_step
                        next_column = current_column + column_step
                        if 0 <= next_row < height and 0 <= next_column < width and ((next_row, next_column) not in seen) and (grid[next_row][next_column] == 1):
                            seen.add((next_row, next_column))
                            stack.append((next_row, next_column))
                components.append(cells)
        output = []
        for source_row in grid:
            output.append([8 if value == 1 else value for value in source_row])
        passed_columns = set()
        for cells in components:
            bottom_shift = height - 1 - max((cell[0] for cell in cells))
            cells_by_row = {}
            for row, column in cells:
                if row not in cells_by_row:
                    cells_by_row[row] = []
                cells_by_row[row].append(column)
            forbidden_shifts = []
            for row, columns in cells_by_row.items():
                has_wide_part = False
                column_set = set(columns)
                for column in columns:
                    if column + 1 in column_set:
                        has_wide_part = True
                        break
                shift_to_separator = separator_row - row
                if has_wide_part and shift_to_separator > 0:
                    forbidden_shifts.append(shift_to_separator)
            shift = bottom_shift
            if forbidden_shifts:
                shift = min(shift, min(forbidden_shifts) - 1)
            for row, column in cells:
                output[row + shift][column] = 1
            if min((row + shift for row, _ in cells)) > separator_row:
                for _, column in cells:
                    passed_columns.add(column)
        for column in passed_columns:
            if output[separator_row][column] == 2:
                output[separator_row][column] = 8
        output = output
    return output
