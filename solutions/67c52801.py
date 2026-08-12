def transform(grid):
    height = len(grid)
    width = len(grid[0])
    base = max(set(grid[-1]), key=grid[-1].count)

    slots = []
    column = 0
    while column < width:
        if grid[-2][column] == 0:
            start = column
            while column < width and grid[-2][column] == 0:
                column += 1
            if (
                start > 0
                and column < width
                and grid[-2][start - 1] == base
                and grid[-2][column] == base
            ):
                slots.append((start, column - start))
        else:
            column += 1

    seen = set()
    objects = []
    for start_row in range(height - 2):
        for start_column in range(width):
            color = grid[start_row][start_column]
            if color in (0, base) or (start_row, start_column) in seen:
                continue
            stack = [(start_row, start_column)]
            seen.add((start_row, start_column))
            area = 0
            while stack:
                row, column = stack.pop()
                area += 1
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if (
                        0 <= next_row < height - 2
                        and 0 <= next_column < width
                        and grid[next_row][next_column] == color
                        and (next_row, next_column) not in seen
                    ):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))
            objects.append((color, area))

    output = [[0 for _ in range(width)] for _ in range(height)]
    output[-1] = grid[-1][:]
    for column in range(width):
        if grid[-2][column] == base:
            output[-2][column] = base

    for start, slot_width in slots:
        for index, (color, area) in enumerate(objects):
            if area == 2 * slot_width:
                for row in (height - 3, height - 2):
                    for column in range(start, start + slot_width):
                        output[row][column] = color
                objects.pop(index)
                break

    return output
