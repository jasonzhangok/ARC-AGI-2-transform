def transform(grid):
    height = len(grid)
    width = len(grid[0])

    color_counts = {}
    blues = []
    magentas = []
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
            if color == 1:
                blues.append((row, col))
            elif color == 6:
                magentas.append((row, col))
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    output = [[background for col in range(width)] for row in range(height)]
    for row, col in blues:
        output[row][col] = 1

    candidates = []
    for blue_row, blue_col in blues:
        for magenta_row, magenta_col in magentas:
            if blue_row == magenta_row or blue_col == magenta_col:
                distance = abs(blue_row - magenta_row) + abs(blue_col - magenta_col)
                candidates.append(
                    (distance, blue_row, blue_col, magenta_row, magenta_col)
                )
    candidates.sort()

    used_blues = set()
    used_magentas = set()
    for distance, blue_row, blue_col, magenta_row, magenta_col in candidates:
        blue = (blue_row, blue_col)
        magenta = (magenta_row, magenta_col)
        if blue in used_blues or magenta in used_magentas:
            continue
        used_blues.add(blue)
        used_magentas.add(magenta)
        row_offset = magenta_row - blue_row
        col_offset = magenta_col - blue_col
        target_row = blue_row - col_offset
        target_col = blue_col + row_offset
        if 0 <= target_row < height and 0 <= target_col < width:
            output[target_row][target_col] = 7

    return output
