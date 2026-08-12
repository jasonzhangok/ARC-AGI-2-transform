def transform(grid):
    try:
        h, w = (len(grid), len(grid[0]))
        if w % 2 == 0 and all((row[:w // 2] == row[w // 2:] for row in grid)):
            raise StopIteration([row[:w // 2] for row in grid])
        raise StopIteration([row[:] for row in grid[:h // 2]])
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
