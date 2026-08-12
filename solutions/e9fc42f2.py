def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    pieces = []

    for start_row in range(height):
        for start_column in range(width):
            if grid[start_row][start_column] == 2 or (start_row, start_column) in seen:
                continue
            stack = [(start_row, start_column)]
            seen.add((start_row, start_column))
            component = []
            while stack:
                row, column = stack.pop()
                component.append((row, column))
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if (
                        0 <= next_row < height
                        and 0 <= next_column < width
                        and grid[next_row][next_column] != 2
                        and (next_row, next_column) not in seen
                    ):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))

            top = min(row for row, column in component)
            bottom = max(row for row, column in component)
            left = min(column for row, column in component)
            right = max(column for row, column in component)
            crop = [
                [grid[row][column] for column in range(left, right + 1)]
                for row in range(top, bottom + 1)
            ]
            markers = [
                (grid[row][column], row - top, column - left)
                for row, column in component
                if grid[row][column] not in (1, 2)
            ]
            pieces.append((crop, markers))

    connectors = {}
    for index, (crop, markers) in enumerate(pieces):
        piece_height = len(crop)
        piece_width = len(crop[0])
        for color, row, column in markers:
            if row == 0:
                direction = (-1, 0)
            elif row == piece_height - 1:
                direction = (1, 0)
            elif column == 0:
                direction = (0, -1)
            else:
                direction = (0, 1)
            connectors.setdefault(color, []).append(
                (index, row, column, direction)
            )

    positions = {0: (0, 0)}
    while len(positions) < len(pieces):
        changed = False
        for matches in connectors.values():
            if len(matches) != 2:
                continue
            first, second = matches
            first_index, first_row, first_column, first_direction = first
            second_index, second_row, second_column, second_direction = second
            if first_index in positions and second_index not in positions:
                base_row, base_column = positions[first_index]
                positions[second_index] = (
                    base_row + first_row + first_direction[0] - second_row,
                    base_column + first_column + first_direction[1] - second_column,
                )
                changed = True
            elif second_index in positions and first_index not in positions:
                base_row, base_column = positions[second_index]
                positions[first_index] = (
                    base_row + second_row + second_direction[0] - first_row,
                    base_column + second_column + second_direction[1] - first_column,
                )
                changed = True
        if not changed:
            break

    min_row = min(positions[index][0] for index in positions)
    min_column = min(positions[index][1] for index in positions)
    max_row = max(
        positions[index][0] + len(pieces[index][0])
        for index in positions
    )
    max_column = max(
        positions[index][1] + len(pieces[index][0][0])
        for index in positions
    )
    output = [
        [2 for _ in range(max_column - min_column)]
        for _ in range(max_row - min_row)
    ]
    for index, (base_row, base_column) in positions.items():
        crop = pieces[index][0]
        for row in range(len(crop)):
            for column in range(len(crop[0])):
                output[base_row - min_row + row][base_column - min_column + column] = crop[row][column]

    return output
