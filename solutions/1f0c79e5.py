def transform(grid):
    height, width = len(grid), len(grid[0])
    nonzero = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] != 0
    ]
    top = min(row for row, _ in nonzero)
    left = min(col for _, col in nonzero)
    drawing_color = next(
        grid[row][col] for row, col in nonzero if grid[row][col] != 2
    )
    colored = {
        (row - top, col - left)
        for row, col in nonzero
        if grid[row][col] == drawing_color
    }
    corners = {(0, 0), (0, 1), (1, 0), (1, 1)}
    base = {(top + row, left + col) for row, col in corners}
    translations = []

    if len(colored) == 3:
        missing = next(iter(corners - colored))
        opposite = 1 - missing[0], 1 - missing[1]
        direction = missing[0] - opposite[0], missing[1] - opposite[1]
        translations.append((direction, range(0, max(height, width) + 1)))
    elif len(colored) == 2:
        direction = (-1, 1) if colored == {(0, 0), (1, 1)} else (1, 1)
        limit = max(height, width)
        translations.append((direction, range(-limit, limit + 1)))
    else:
        only = next(iter(colored))
        opposite = 1 - only[0], 1 - only[1]
        direction = opposite[0] - only[0], opposite[1] - only[1]
        limit = max(height, width)
        translations.append((direction, range(0, limit + 1)))
        translations.append(((-direction[0], direction[1]), range(-limit, limit + 1)))

    painted = set()
    for (row_step, col_step), repetitions in translations:
        for repetition in repetitions:
            for row, col in base:
                target = row + repetition * row_step, col + repetition * col_step
                if 0 <= target[0] < height and 0 <= target[1] < width:
                    painted.add(target)
    return [
        [drawing_color if (row, col) in painted else 0 for col in range(width)]
        for row in range(height)
    ]
