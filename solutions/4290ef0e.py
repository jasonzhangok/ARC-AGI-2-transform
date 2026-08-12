def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    colors = [color for color in counts if color != background]
    recovered = []

    for color in colors:
        points = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    points.add((row, col))

        answer = None
        for size in range(1, 2 * max(height, width) + 2, 2):
            if answer is not None:
                break
            for top in range(-size + 1, height):
                if answer is not None:
                    break
                for left in range(-size + 1, width):
                    if not all(0 <= row - top < size and 0 <= col - left < size
                               for row, col in points):
                        continue
                    pattern = set()
                    for row, col in points:
                        x = row - top
                        y = col - left
                        pattern.add((x, y))
                        pattern.add((x, size - 1 - y))
                        pattern.add((size - 1 - x, y))
                        pattern.add((size - 1 - x, size - 1 - y))
                        pattern.add((y, x))
                        pattern.add((y, size - 1 - x))
                        pattern.add((size - 1 - y, x))
                        pattern.add((size - 1 - y, size - 1 - x))
                    visible = set()
                    for x, y in pattern:
                        row = top + x
                        col = left + y
                        if 0 <= row < height and 0 <= col < width:
                            visible.add((row, col))
                    if visible == points:
                        answer = (size, pattern)
                        break
        recovered.append((color, answer[0], answer[1]))

    output_size = max(size for _, size, _ in recovered)
    output = [[background for _ in range(output_size)] for _ in range(output_size)]
    for color, size, pattern in recovered:
        offset = (output_size - size) // 2
        for row, col in pattern:
            output[offset + row][offset + col] = color
    return output
