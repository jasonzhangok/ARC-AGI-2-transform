def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    visited = set()

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0 or (start_row, start_col) in visited:
                continue
            component = []
            frontier = [(start_row, start_col)]
            visited.add((start_row, start_col))
            while frontier:
                row, col = frontier.pop()
                component.append((row, col))
                for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (0 <= next_row < height and 0 <= next_col < width
                            and grid[next_row][next_col] != 0
                            and (next_row, next_col) not in visited):
                        visited.add((next_row, next_col))
                        frontier.append((next_row, next_col))

            top = min(point[0] for point in component)
            bottom = max(point[0] for point in component)
            left = min(point[1] for point in component)
            right = max(point[1] for point in component)
            outer_color = grid[top][left]
            inner_color = outer_color
            for row, col in component:
                if grid[row][col] != outer_color:
                    inner_color = grid[row][col]
                    break
            inner_height = bottom - top - 1
            inner_width = right - left - 1

            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if row == top or row == bottom or col == left or col == right:
                        output[row][col] = inner_color
                    else:
                        output[row][col] = outer_color
            for row in range(max(0, top - inner_height), top):
                for col in range(left, right + 1):
                    output[row][col] = outer_color
            for row in range(bottom + 1, min(height, bottom + inner_height + 1)):
                for col in range(left, right + 1):
                    output[row][col] = outer_color
            for row in range(top, bottom + 1):
                for col in range(max(0, left - inner_width), left):
                    output[row][col] = outer_color
                for col in range(right + 1, min(width, right + inner_width + 1)):
                    output[row][col] = outer_color
    return output
