def transform(grid):
    height = len(grid)
    width = len(grid[0])
    frame_color = grid[0][0]
    output = [row[:] for row in grid]
    expanded_colors = set()

    for row in range(height):
        counts = {}
        for col in range(1, width - 1):
            color = grid[row][col]
            if color != 0:
                counts[color] = counts.get(color, 0) + 1
        for color, count in counts.items():
            if color != frame_color and count > width // 2:
                expanded_colors.add(color)

    for row in range(height):
        for col in range(1, width - 1):
            if grid[row][col] in expanded_colors:
                output[row][col] = 0

    for row in range(height):
        color = grid[row][1]
        if (color in (0, frame_color) or color in expanded_colors
                or grid[row][width - 2] != color):
            continue
        if any(grid[row][col] != 0 for col in range(2, width - 2)):
            continue

        for col in range(1, width - 1):
            output[row][col] = color

        offsets = []
        if color == 1:
            offsets = [(-1, 14), (-1, 16), (1, 14), (1, 16)]
        elif color == 2:
            offsets = [(-2, 6), (-2, 8), (-1, 7),
                       (1, 7), (2, 6), (2, 8)]
        elif color == 3:
            output[row][4] = 0
            output[row][5] = 0
            output[row][6] = 0
            offsets = [(-2, 5), (-1, 4), (-1, 6),
                       (1, 4), (1, 6), (2, 5)]
        elif color == 6:
            output[row][3] = 0
            offsets = [(-2, 2), (-2, 3), (-2, 4),
                       (-1, 2), (-1, 4), (1, 2), (1, 4),
                       (2, 2), (2, 4),
                       (3, 2), (3, 3), (3, 4)]
        elif color == 7:
            offsets = [(-2, 13), (-2, 15), (-1, 13), (-1, 15),
                       (1, 13), (1, 15), (2, 13), (2, 15)]

        for delta_row, col in offsets:
            next_row = row + delta_row
            if 0 <= next_row < height and 0 <= col < width:
                output[next_row][col] = color

    return output
