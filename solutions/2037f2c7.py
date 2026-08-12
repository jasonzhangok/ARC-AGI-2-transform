def transform(grid):
    height = len(grid)
    width = len(grid[0])

    seen = []
    for row_index in range(height):
        seen.append([False] * width)

    components = []
    for row_index in range(height):
        for column_index in range(width):
            if grid[row_index][column_index] == 0 or seen[row_index][column_index]:
                continue

            cells = []
            stack = [(row_index, column_index)]
            seen[row_index][column_index] = True
            while stack:
                current_row, current_column = stack.pop()
                cells.append((current_row, current_column))
                neighbors = (
                    (current_row - 1, current_column),
                    (current_row + 1, current_column),
                    (current_row, current_column - 1),
                    (current_row, current_column + 1),
                )
                for neighbor_row, neighbor_column in neighbors:
                    if (0 <= neighbor_row < height
                            and 0 <= neighbor_column < width
                            and grid[neighbor_row][neighbor_column] != 0
                            and not seen[neighbor_row][neighbor_column]):
                        seen[neighbor_row][neighbor_column] = True
                        stack.append((neighbor_row, neighbor_column))
            components.append(cells)

    objects = []
    for cells in components:
        top = cells[0][0]
        bottom = cells[0][0]
        left = cells[0][1]
        right = cells[0][1]
        for row_index, column_index in cells:
            if row_index < top:
                top = row_index
            if row_index > bottom:
                bottom = row_index
            if column_index < left:
                left = column_index
            if column_index > right:
                right = column_index

        local = []
        for row_index in range(bottom - top + 1):
            local.append([0] * (right - left + 1))
        for row_index, column_index in cells:
            local[row_index - top][column_index - left] = grid[row_index][column_index]
        objects.append(local)

    first_count = 0
    for row in objects[0]:
        for color in row:
            if color != 0:
                first_count += 1
    second_count = 0
    for row in objects[1]:
        for color in row:
            if color != 0:
                second_count += 1

    if first_count > second_count:
        complete = objects[0]
        damaged = objects[1]
    else:
        complete = objects[1]
        damaged = objects[0]

    mask = []
    first_missing_row = len(complete)
    last_missing_row = -1
    first_missing_column = len(complete[0])
    last_missing_column = -1
    for row_index in range(len(complete)):
        mask_row = []
        for column_index in range(len(complete[0])):
            if (complete[row_index][column_index] != 0
                    and damaged[row_index][column_index] == 0):
                mask_row.append(8)
                if row_index < first_missing_row:
                    first_missing_row = row_index
                if row_index > last_missing_row:
                    last_missing_row = row_index
                if column_index < first_missing_column:
                    first_missing_column = column_index
                if column_index > last_missing_column:
                    last_missing_column = column_index
            else:
                mask_row.append(0)
        mask.append(mask_row)

    output = []
    for row_index in range(first_missing_row, last_missing_row + 1):
        output_row = []
        for column_index in range(first_missing_column, last_missing_column + 1):
            output_row.append(mask[row_index][column_index])
        output.append(output_row)
    return output
