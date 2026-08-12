

def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)

    top_color = {}
    for cell_value in (grid[0][1:-1]):
        top_color[cell_value] = top_color.get(cell_value, 0) + 1
    top_color = max(top_color, key=top_color.get)
    bottom_color = {}
    for cell_value in (grid[-1][1:-1]):
        bottom_color[cell_value] = bottom_color.get(cell_value, 0) + 1
    bottom_color = max(bottom_color, key=bottom_color.get)
    left_color = {}
    for cell_value in (row[0] for row in grid[1:-1]):
        left_color[cell_value] = left_color.get(cell_value, 0) + 1
    left_color = max(left_color, key=left_color.get)
    right_color = {}
    for cell_value in (row[-1] for row in grid[1:-1]):
        right_color[cell_value] = right_color.get(cell_value, 0) + 1
    right_color = max(right_color, key=right_color.get)
    directions = {
        top_color: (-1, 0),
        bottom_color: (1, 0),
        left_color: (0, -1),
        right_color: (0, 1),
    }

    moves = {}
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            color = grid[row][col]
            if color not in directions:
                continue
            row_step, col_step = directions[color]
            target_row = row + row_step
            target_col = col + col_step
            if not (
                1 <= target_row < height - 1
                and 1 <= target_col < width - 1
            ):
                continue
            moves[(row, col)] = (target_row, target_col, color)

    while moves:
        target_counts = {}
        for cell_value in ((target_row, target_col)
            for target_row, target_col, _ in moves.values()):
            target_counts[cell_value] = target_counts.get(cell_value, 0) + 1
        moving_sources = set(moves)
        blocked = [
            source
            for source, (target_row, target_col, _) in moves.items()
            if target_counts[(target_row, target_col)] > 1
            or (
                grid[target_row][target_col] != background
                and (target_row, target_col) not in moving_sources
            )
        ]
        if not blocked:
            break
        for source in blocked:
            del moves[source]

    output = [row[:] for row in grid]
    for row, col in moves:
        output[row][col] = background
    for target_row, target_col, color in moves.values():
        output[target_row][target_col] = color

    return output
