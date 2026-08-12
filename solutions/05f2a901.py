def transform(grid):
    output = [row[:] for row in grid]
    moving = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 2
    ]
    target = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 8
    ]

    top, bottom = min(r for r, _ in moving), max(r for r, _ in moving)
    left, right = min(c for _, c in moving), max(c for _, c in moving)
    target_top, target_bottom = min(r for r, _ in target), max(r for r, _ in target)
    target_left, target_right = min(c for _, c in target), max(c for _, c in target)
    dr = dc = 0

    if bottom < target_top:
        dr = target_top - bottom - 1
    elif target_bottom < top:
        dr = -(top - target_bottom - 1)
    elif right < target_left:
        dc = target_left - right - 1
    else:
        dc = -(left - target_right - 1)

    for r, c in moving:
        output[r][c] = 0
    for r, c in moving:
        output[r + dr][c + dc] = 2
    return output
