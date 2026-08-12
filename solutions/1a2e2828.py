def transform(grid):
    try:
        colors = {value for row in grid for value in row if value != 0}
        for color in colors:
            if any((all((value == color for value in row)) for row in grid)):
                raise StopIteration([[color]])
            for col in range(len(grid[0])):
                if all((grid[row][col] == color for row in range(len(grid)))):
                    raise StopIteration([[color]])
        raise ValueError('no uninterrupted full-length colored line')
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
