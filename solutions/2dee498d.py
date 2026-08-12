def transform(grid):
    try:
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
                raise StopIteration(first)
        raise StopIteration([row[:] for row in grid])
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
