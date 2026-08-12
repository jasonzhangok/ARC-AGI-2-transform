def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seed_row = 0
    seed_column = 0
    walls = set()
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 1:
                seed_row, seed_column = row, column
            elif grid[row][column] == 2:
                walls.add((row, column))

    output = [row[:] for row in grid]
    output[seed_row][seed_column] = 0
    falling_columns = {seed_column}
    passed_row = seed_row
    settled = False
    while not settled:
        top = None
        left = None
        right = None
        for row in range(passed_row + 1, height):
            wall_columns = [column for column in range(width) if grid[row][column] == 2]
            for falling_column in falling_columns:
                left_candidates = [column for column in wall_columns if column < falling_column]
                right_candidates = [column for column in wall_columns if column > falling_column]
                if left_candidates and right_candidates:
                    top = row
                    left = max(left_candidates)
                    right = min(right_candidates)
                    break
            if top is not None:
                break
        if top is None:
            output[-1] = [1 for column in range(width)]
            break
        bottom = top
        while (bottom + 1 < height
               and grid[bottom + 1][left] == 2
               and grid[bottom + 1][right] == 2):
            bottom += 1
        region = set()
        stack = [(top, column) for column in falling_columns if left < column < right]
        while stack:
            row, column = stack.pop()
            if ((row, column) in region
                    or not (top <= row < bottom and left < column < right)
                    or grid[row][column] == 2):
                continue
            region.add((row, column))
            stack.extend(((row - 1, column), (row + 1, column),
                          (row, column - 1), (row, column + 1)))
        exits = set(column for column in range(left + 1, right)
                    if grid[bottom][column] == 0)
        if exits:
            falling_columns = exits
            passed_row = bottom
        else:
            for row, column in region:
                output[row][column] = 1
            settled = True
    return output
