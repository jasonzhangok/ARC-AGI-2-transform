def transform(grid):
    height = len(grid)
    width = len(grid[0])
    arm = height // 2
    output = [[8] * width for _ in range(height)]

    for color in set(value for row in grid for value in row) - {8}:
        remaining = {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        while remaining:
            pending = [remaining.pop()]
            component = set(pending)
            while pending:
                row, col = pending.pop()
                for neighbor in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        pending.append(neighbor)
            top = min(row for row, _ in component)
            left = min(col for _, col in component)
            shape = {(row - top, col - left) for row, col in component}

            if shape == {(0, 0), (0, 1), (1, 0)}:
                for offset in range(arm):
                    output[0][offset] = color
                    output[offset][0] = color
            elif shape == {(0, 0), (0, 1), (1, 1)}:
                for offset in range(arm):
                    output[0][width - 1 - offset] = color
                    output[offset][width - 1] = color
            elif shape == {(0, 0), (1, 0), (1, 1)}:
                for offset in range(arm):
                    output[height - 1][offset] = color
                    output[height - 1 - offset][0] = color
            else:
                for offset in range(arm):
                    output[height - 1][width - 1 - offset] = color
                    output[height - 1 - offset][width - 1] = color
    return output
