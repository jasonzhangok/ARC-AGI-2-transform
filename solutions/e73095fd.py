def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    visited = set()

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] != 0 or (start_row, start_col) in visited:
                continue
            component = []
            frontier = [(start_row, start_col)]
            visited.add((start_row, start_col))
            while frontier:
                row, col = frontier.pop()
                component.append((row, col))
                for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (0 <= next_row < height and 0 <= next_col < width
                            and grid[next_row][next_col] == 0
                            and (next_row, next_col) not in visited):
                        visited.add((next_row, next_col))
                        frontier.append((next_row, next_col))

            min_row = min(point[0] for point in component)
            max_row = max(point[0] for point in component)
            min_col = min(point[1] for point in component)
            max_col = max(point[1] for point in component)
            solid = len(component) == (max_row - min_row + 1) * (max_col - min_col + 1)
            clean = solid and min_row > 0 and max_row < height - 1

            if clean:
                for border_row in (min_row - 1, max_row + 1):
                    for col in (min_col - 2, max_col + 2):
                        if 0 <= col < width and grid[border_row][col] == 5:
                            clean = False
                for border_col in (min_col - 1, max_col + 1):
                    if 0 <= border_col < width:
                        for row in (min_row - 2, max_row + 2):
                            if 0 <= row < height and grid[row][border_col] == 5:
                                clean = False

            if clean:
                for row, col in component:
                    output[row][col] = 4
    return output
