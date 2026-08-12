def transform(grid):
    try:
        height = len(grid)
        width = len(grid[0])
        remaining = {(row, col) for row in range(height) for col in range(width) if grid[row][col] not in (0, 1)}
        blocks = []
        while remaining:
            pending = [remaining.pop()]
            component = set(pending)
            while pending:
                row, col = pending.pop()
                for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        pending.append(neighbor)
            top = min((row for row, _ in component))
            bottom = max((row for row, _ in component))
            left = min((col for _, col in component))
            right = max((col for _, col in component))
            color = grid[next(iter(component))[0]][next(iter(component))[1]]
            blocks.append(((top + bottom) // 2, (left + right) // 2, color))
        row_positions = sorted({row for row, _, _ in blocks})
        col_positions = sorted({col for _, col, _ in blocks})
        row_index = {row: index for index, row in enumerate(row_positions)}
        col_index = {col: index for index, col in enumerate(col_positions)}
        macro = [[0] * len(col_positions) for _ in row_positions]
        for row, col, color in blocks:
            macro[row_index[row]][col_index[col]] = color
        if all((value == 1 for value in grid[0])):
            raise StopIteration([[0] * (len(row) - len(values)) + values for row in macro for values in [[value for value in row if value != 0]]])
        if all((value == 1 for value in grid[-1])):
            raise StopIteration([values + [0] * (len(row) - len(values)) for row in macro for values in [[value for value in row if value != 0]]])
        output = [[0] * len(macro[0]) for _ in macro]
        downward = all((row[-1] == 1 for row in grid))
        for col in range(len(macro[0])):
            values = [macro[row][col] for row in range(len(macro)) if macro[row][col] != 0]
            start = len(macro) - len(values) if downward else 0
            for offset, value in enumerate(values):
                output[start + offset][col] = value
        raise StopIteration(output)
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
