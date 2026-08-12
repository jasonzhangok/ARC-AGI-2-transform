def transform(grid):
    try:
        'Straighten all foreground cells into a centered horizontal line.'
        height = len(grid)
        if height == 0:
            raise StopIteration([])
        width = len(grid[0])
        counts = {}
        for cell_value in (value for row in grid for value in row):
            counts[cell_value] = counts.get(cell_value, 0) + 1
        background = max(counts, key=counts.get)
        foreground = [value for value in counts if value != background]
        output = [[background for _ in range(width)] for _ in range(height)]
        if not foreground:
            raise StopIteration(output)
        color = foreground[0]
        length = sum((value != background for row in grid for value in row))
        row = height // 2
        start = (width - length) // 2
        for column in range(start, start + length):
            output[row][column] = color
        raise StopIteration(output)
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
