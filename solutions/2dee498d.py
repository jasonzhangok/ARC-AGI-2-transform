def transform(grid):
    width = len(grid[0])
    for period in range(1, width + 1):
        if width % period != 0:
            continue
        first = [row[:period] for row in grid]
        valid = True
        for start in range(0, width, period):
            block = [row[start:start + period] for row in grid]
            mirrored = [row[::-1] for row in first]
            if block != first and block != mirrored:
                valid = False
                break
        if valid:
            return first
    return [row[:] for row in grid]
