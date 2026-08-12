def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set()
    for row in grid:
        for value in row:
            if value != 0:
                colors.add(value)
    if len(colors) != 2:
        output = [row[:] for row in grid]
    else:
        boxes = []
        for color in colors:
            cells = []
            for row in range(height):
                for column in range(width):
                    if grid[row][column] == color:
                        cells.append((row, column))
            top = min((cell[0] for cell in cells))
            bottom = max((cell[0] for cell in cells))
            left = min((cell[1] for cell in cells))
            right = max((cell[1] for cell in cells))
            area = (bottom - top + 1) * (right - left + 1)
            boxes.append((area, len(cells), top, bottom, left, right, color))
        boxes.sort(reverse=True)
        outer = boxes[0]
        inner = boxes[1]
        inner_height = inner[3] - inner[2] + 1
        inner_width = inner[5] - inner[4] + 1
        thickness = min(inner_height, inner_width, outer[2], outer[4], height - 1 - outer[3], width - 1 - outer[5])
        output = [row[:] for row in grid]
        for row in range(outer[2] - thickness, outer[3] + thickness + 1):
            for column in range(outer[4] - thickness, outer[5] + thickness + 1):
                if output[row][column] == 0:
                    output[row][column] = inner[6]
        output = output
    return output
