def transform(grid):
    height = len(grid)
    width = len(grid[0])
    background = 7
    output = [[background for _ in range(width)] for _ in range(height)]
    seen = set()

    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in seen:
                continue

            color = grid[row][col]
            component = []
            queue = [(row, col)]
            seen.add((row, col))
            index = 0
            while index < len(queue):
                current_row, current_col = queue[index]
                index += 1
                component.append((current_row, current_col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and (next_row, next_col) not in seen
                            and grid[next_row][next_col] == color):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))

            distance = len(component)
            for current_row, current_col in component:
                next_row = current_row + distance
                if next_row < height:
                    output[next_row][current_col] = color

    return output
