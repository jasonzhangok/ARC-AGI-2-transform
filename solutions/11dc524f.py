def transform(grid):
    background = 7
    height, width = len(grid), len(grid[0])
    red = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 2]
    gray = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 5]
    red_top, red_bottom = min(r for r, _ in red), max(r for r, _ in red)
    red_left, red_right = min(c for _, c in red), max(c for _, c in red)
    gray_top, gray_bottom = min(r for r, _ in gray), max(r for r, _ in gray)
    gray_left, gray_right = min(c for _, c in gray), max(c for _, c in gray)
    object_height, object_width = red_bottom - red_top + 1, red_right - red_left + 1
    shape = {(r - red_top, c - red_left) for r, c in red}
    output = [[background] * width for _ in range(height)]

    if red_right < gray_left:
        gray_target_top, gray_target_left = red_top, gray_left
        red_target_top, red_target_left = red_top, gray_left - object_width
        reflected = {(r, object_width - 1 - c) for r, c in shape}
    elif gray_right < red_left:
        gray_target_top, gray_target_left = red_top, gray_right - object_width + 1
        red_target_top, red_target_left = red_top, gray_right + 1
        reflected = {(r, object_width - 1 - c) for r, c in shape}
    elif red_bottom < gray_top:
        gray_target_top, gray_target_left = gray_top, red_left
        red_target_top, red_target_left = gray_top - object_height, red_left
        reflected = {(object_height - 1 - r, c) for r, c in shape}
    else:
        gray_target_top, gray_target_left = gray_bottom - object_height + 1, red_left
        red_target_top, red_target_left = gray_bottom + 1, red_left
        reflected = {(object_height - 1 - r, c) for r, c in shape}

    for r, c in shape:
        output[red_target_top + r][red_target_left + c] = 2
    for r, c in reflected:
        output[gray_target_top + r][gray_target_left + c] = 5
    return output
