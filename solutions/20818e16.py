

def transform(grid):
    background = {}
    for cell_value in (value for row in grid for value in row):
        background[cell_value] = background.get(cell_value, 0) + 1
    background = max(background, key=background.get)
    rectangles = []
    for color in {value for row in grid for value in row if value != background}:
        points = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color]
        top, bottom = min(r for r, _ in points), max(r for r, _ in points)
        left, right = min(c for _, c in points), max(c for _, c in points)
        rectangles.append(((bottom - top + 1) * (right - left + 1), bottom - top + 1, right - left + 1, color))
    rectangles.sort(reverse=True)
    height = max(item[1] for item in rectangles)
    width = max(item[2] for item in rectangles)
    output = [[background] * width for _ in range(height)]
    for _, rect_height, rect_width, color in rectangles:
        for row in range(rect_height):
            for col in range(rect_width):
                output[row][col] = color
    return output
