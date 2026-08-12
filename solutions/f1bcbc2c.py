def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    result = [row[:] for row in grid]
    if not height or not width:
        return result

    walls = [column for column in range(width) if grid[0][column] == 7]
    if len(walls) < 2:
        return result

    pending = []
    seen = set()
    left = walls[0]
    right = walls[-1]
    for column in range(left + 1, right):
        value = grid[0][column]
        passable = value == 0 or (
            value == 9
            and column > 0
            and column + 1 < width
            and grid[0][column - 1] == 7
            and grid[0][column + 1] == 7
        )
        if passable:
            pending.append((0, column))
            seen.add((0, column))

    index = 0
    while index < len(pending):
        row, column = pending[index]
        index += 1
        result[row][column] = 8
        for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_step
            next_column = column + column_step
            if not (0 <= next_row < height and 0 <= next_column < width):
                continue
            if (next_row, next_column) in seen:
                continue
            value = grid[next_row][next_column]
            passable = value == 0 or (
                value == 9
                and next_column > 0
                and next_column + 1 < width
                and grid[next_row][next_column - 1] == 7
                and grid[next_row][next_column + 1] == 7
            )
            if passable:
                seen.add((next_row, next_column))
                pending.append((next_row, next_column))

    return result
