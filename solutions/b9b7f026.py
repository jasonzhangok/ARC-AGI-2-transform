def transform(grid):
    try:
        colors = {value for row in grid for value in row if value != 0}
        for color in colors:
            cells = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color]
            height = max((r for r, _ in cells)) - min((r for r, _ in cells)) + 1
            width = max((c for _, c in cells)) - min((c for _, c in cells)) + 1
            if len(cells) != height * width:
                raise StopIteration([[color]])
        raise StopIteration([[]])
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
