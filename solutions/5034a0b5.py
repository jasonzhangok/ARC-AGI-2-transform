from collections import Counter


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]

    top_color = Counter(grid[0][1:-1]).most_common(1)[0][0]
    bottom_color = Counter(grid[-1][1:-1]).most_common(1)[0][0]
    left_color = Counter(row[0] for row in grid[1:-1]).most_common(1)[0][0]
    right_color = Counter(row[-1] for row in grid[1:-1]).most_common(1)[0][0]
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
        target_counts = Counter(
            (target_row, target_col)
            for target_row, target_col, _ in moves.values()
        )
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
