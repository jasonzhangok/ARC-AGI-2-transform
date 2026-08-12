def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    seen = set()

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] != 0 or (start_row, start_col) in seen:
                continue
            component = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            boundary = {1: set(), 2: set()}

            for row, col in queue:
                component.append((row, col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + delta_row, col + delta_col)
                    if not (0 <= neighbor[0] < height and 0 <= neighbor[1] < width):
                        continue
                    color = grid[neighbor[0]][neighbor[1]]
                    if color == 0 and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
                    elif color == 1 or color == 2:
                        boundary[color].add(neighbor)

            fill_color = 1 if len(boundary[1]) > len(boundary[2]) else 2
            for row, col in component:
                output[row][col] = fill_color

    return output
