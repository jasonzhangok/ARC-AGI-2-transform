def transform(grid):
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    background = max(counts, key=counts.get)
    output = [row[:] for row in grid]
    objects = []
    template = set()

    for color in counts:
        if color == background:
            continue
        cells = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == color:
                    cells.append((row, col))
        top = min(row for row, col in cells)
        left = min(col for row, col in cells)
        objects.append((color, top, left))
        for row, col in cells:
            template.add((row - top, col - left))

    for color, top, left in objects:
        for row, col in template:
            output[top + row][left + col] = color
    return output
