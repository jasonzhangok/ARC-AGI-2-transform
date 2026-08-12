def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = [5, 2, 8, 9, 6]
    counts = []

    for color in colors:
        remaining = {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        count = 0
        while remaining:
            count += 1
            pending = [remaining.pop()]
            while pending:
                row, col = pending.pop()
                for drow in (-1, 0, 1):
                    for dcol in (-1, 0, 1):
                        if drow == 0 and dcol == 0:
                            continue
                        neighbor = (row + drow, col + dcol)
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            pending.append(neighbor)
        counts.append(count)

    output_height = max(counts)
    output = [[7] * len(colors) for _ in range(output_height)]
    for col, (color, count) in enumerate(zip(colors, counts)):
        for row in range(output_height - count, output_height):
            output[row][col] = color
    return output
