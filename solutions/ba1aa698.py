from collections import Counter


def transform(grid):
    """Predict the next framed panel in the object's vertical sequence."""
    height = len(grid)
    frame = grid[0][0]

    separators = [
        col
        for col in range(len(grid[0]))
        if all(grid[row][col] == frame for row in range(height))
    ]
    panels = list(zip(separators, separators[1:]))

    interior_values = [
        grid[row][col]
        for left, right in panels
        for row in range(1, height - 1)
        for col in range(left + 1, right)
    ]
    background = Counter(interior_values).most_common(1)[0][0]

    objects = []
    for left, right in panels:
        cells = [
            (row, col - left, grid[row][col])
            for row in range(1, height - 1)
            for col in range(left + 1, right)
            if grid[row][col] != background
        ]
        objects.append(cells)

    tops = [min(row for row, _, _ in cells) for cells in objects]
    first = objects[0]
    first_top = tops[0]
    first_left = min(col for _, col, _ in first)
    shape_height = max(row for row, _, _ in first) - first_top + 1

    if len(tops) == 1:
        vertical_step = 0
    else:
        steps = [b - a for a, b in zip(tops, tops[1:])]
        vertical_step = Counter(steps).most_common(1)[0][0]
    next_top = tops[-1] + vertical_step

    # A downward sequence can end one raster cell short when evenly sampled
    # between its initial position and the vertically reflected endpoint.
    reflected_top = height - first_top - shape_height
    if vertical_step > 0 and 0 <= reflected_top - next_top <= 1:
        next_top = reflected_top

    panel_width = panels[0][1] - panels[0][0] + 1
    output = [[background] * panel_width for _ in range(height)]
    output[0] = [frame] * panel_width
    output[-1] = [frame] * panel_width
    for row in range(1, height - 1):
        output[row][0] = frame
        output[row][-1] = frame

    next_left = first_left
    for row, col, color in first:
        output[next_top + row - first_top][next_left + col - first_left] = color
    return output
