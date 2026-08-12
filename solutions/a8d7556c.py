def transform(grid):
    height = len(grid)
    width = len(grid[0])
    rectangles = []

    for top in range(height - 1):
        for bottom in range(top + 1, height):
            rect_height = bottom - top + 1
            for left in range(width - 1):
                for right in range(left + 1, width):
                    rect_width = right - left + 1
                    if rect_height != 2 and rect_width != 2:
                        continue
                    cells = frozenset(
                        (row, col)
                        for row in range(top, bottom + 1)
                        for col in range(left, right + 1)
                    )
                    if all(grid[row][col] == 0 for row, col in cells):
                        rectangles.append(cells)

    maximal = [
        rectangle
        for rectangle in rectangles
        if not any(rectangle < other for other in rectangles)
    ]

    selected = []
    occupied = set()
    for rectangle in sorted(maximal, key=len, reverse=True):
        if rectangle.isdisjoint(occupied):
            selected.append(rectangle)
            occupied.update(rectangle)

    output = [row[:] for row in grid]
    for rectangle in selected:
        for row, col in rectangle:
            output[row][col] = 2
    return output
