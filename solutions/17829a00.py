def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    output = [[background] * width for _ in range(height)]
    output[0] = grid[0][:]
    output[-1] = grid[-1][:]

    for color, direction in ((grid[0][0], -1), (grid[-1][0], 1)):
        remaining = set()
        for row in range(1, height - 1):
            for col in range(width):
                if grid[row][col] == color:
                    remaining.add((row, col))

        while remaining:
            start = remaining.pop()
            component = {start}
            queue = [start]
            index = 0
            while index < len(queue):
                row, col = queue[index]
                index += 1
                for row_step in (-1, 0, 1):
                    for col_step in (-1, 0, 1):
                        if row_step == 0 and col_step == 0:
                            continue
                        neighbor = (row + row_step, col + col_step)
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            component.add(neighbor)
                            queue.append(neighbor)

            if direction < 0:
                shift = 1 - min(row for row, col in component)
            else:
                shift = height - 2 - max(row for row, col in component)

            vertical_bar = len({col for row, col in component}) == 1
            overlaps = any((row + shift, col) in component for row, col in component)
            if direction > 0 and vertical_bar and overlaps:
                for row, col in component:
                    output[row][col] = color
            for row, col in component:
                output[row + shift][col] = color

    return output
