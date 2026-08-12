def transform(grid):
    output = [row[:] for row in grid]
    height = len(grid)
    width = len(grid[0]) if height else 0
    for row in range(height):
        boundaries = []
        for col in range(width):
            if grid[row][col] == 2:
                boundaries.append(col)
        if len(boundaries) < 2:
            continue
        left = min(boundaries)
        right = max(boundaries)
        color = None
        for col in range(left - 1, -1, -1):
            if grid[row][col] not in (0, 2):
                color = grid[row][col]
                break
        if color is not None:
            for col in range(left + 1, right):
                if grid[row][col] != 0:
                    break
                if output[row][col] == 0:
                    output[row][col] = color
        color = None
        for col in range(right + 1, width):
            if grid[row][col] not in (0, 2):
                color = grid[row][col]
                break
        if color is not None:
            for col in range(right - 1, left, -1):
                if grid[row][col] != 0:
                    break
                if output[row][col] == 0:
                    output[row][col] = color
    for col in range(width):
        boundaries = []
        for row in range(height):
            if grid[row][col] == 2:
                boundaries.append(row)
        if len(boundaries) < 2:
            continue
        top = min(boundaries)
        bottom = max(boundaries)
        color = None
        for row in range(top - 1, -1, -1):
            if grid[row][col] not in (0, 2):
                color = grid[row][col]
                break
        if color is not None:
            for row in range(top + 1, bottom):
                if grid[row][col] != 0:
                    break
                if output[row][col] == 0:
                    output[row][col] = color
        color = None
        for row in range(bottom + 1, height):
            if grid[row][col] not in (0, 2):
                color = grid[row][col]
                break
        if color is not None:
            for row in range(bottom - 1, top, -1):
                if grid[row][col] != 0:
                    break
                if output[row][col] == 0:
                    output[row][col] = color
    return output
