def transform(grid):
    height = len(grid)
    width = len(grid[0])
    color_counts = {}
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                color = grid[row][col]
                color_counts[color] = color_counts.get(color, 0) + 1
    main_color = 0
    main_count = -1
    for color in color_counts:
        if color_counts[color] > main_count:
            main_color = color
            main_count = color_counts[color]

    rectangles = []
    for top in range(height):
        for bottom in range(top + 1, height):
            for left in range(width):
                for right in range(left + 1, width):
                    full = True
                    for row in range(top, bottom + 1):
                        for col in range(left, right + 1):
                            if grid[row][col] == 0:
                                full = False
                    if full:
                        rectangles.append((top, bottom, left, right))

    maximal_rectangles = []
    for rectangle in rectangles:
        top, bottom, left, right = rectangle
        contained = False
        for other in rectangles:
            if other == rectangle:
                continue
            if other[0] <= top and bottom <= other[1]:
                if other[2] <= left and right <= other[3]:
                    contained = True
        if not contained:
            maximal_rectangles.append(rectangle)

    output = [[0 for col in range(width)] for row in range(height)]
    for top, bottom, left, right in maximal_rectangles:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                output[row][col] = main_color
    return output
