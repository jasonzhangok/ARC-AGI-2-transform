def transform(grid):
    height = len(grid)
    width = len(grid[0])

    candidates = []
    for row in range(height - 1):
        for column in range(width - 1):
            if all(
                grid[r][c] == 5
                for r in (row, row + 1)
                for c in (column, column + 1)
            ):
                candidates.append((row, column))

    best_score = None
    best_choice = 0
    for choice in range(1 << len(candidates)):
        selected = [
            candidates[index]
            for index in range(len(candidates))
            if choice & (1 << index)
        ]
        valid = True
        for first in range(len(selected)):
            row1, column1 = selected[first]
            for second in range(first + 1, len(selected)):
                row2, column2 = selected[second]
                if (
                    (abs(row1 - row2) < 2 and abs(column1 - column2) < 2)
                    or (row1 == row2 and abs(column1 - column2) == 2)
                    or (column1 == column2 and abs(row1 - row2) == 2)
                ):
                    valid = False
        if not valid:
            continue

        square_cells = set()
        for row, column in selected:
            square_cells.update(
                (
                    (row, column),
                    (row + 1, column),
                    (row, column + 1),
                    (row + 1, column + 1),
                )
            )
        residual = {
            (row, column)
            for row in range(height)
            for column in range(width)
            if grid[row][column] == 5 and (row, column) not in square_cells
        }
        isolated = 0
        branches = 0
        for row, column in residual:
            degree = sum(
                (row + dr, column + dc) in residual
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
            )
            isolated += degree == 0
            branches += degree >= 3
        score = (len(selected), -isolated, -branches)
        if best_score is None or score > best_score:
            best_score = score
            best_choice = choice

    output = [row[:] for row in grid]
    for row in range(height):
        for column in range(width):
            if output[row][column] == 5:
                output[row][column] = 2
    for index, (row, column) in enumerate(candidates):
        if best_choice & (1 << index):
            for r in (row, row + 1):
                for c in (column, column + 1):
                    output[r][c] = 8

    return output
