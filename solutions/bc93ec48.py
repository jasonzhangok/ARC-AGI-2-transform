def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    visited = set()
    corner_objects = []

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 7 or (start_row, start_col) in visited:
                continue
            color = grid[start_row][start_col]
            component = []
            frontier = [(start_row, start_col)]
            visited.add((start_row, start_col))
            while frontier:
                row, col = frontier.pop()
                component.append((row, col))
                for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (0 <= next_row < height and 0 <= next_col < width
                            and grid[next_row][next_col] == color
                            and (next_row, next_col) not in visited):
                        visited.add((next_row, next_col))
                        frontier.append((next_row, next_col))

            top = min(point[0] for point in component)
            bottom = max(point[0] for point in component)
            left = min(point[1] for point in component)
            right = max(point[1] for point in component)
            corner = ""
            if top == 0 and left == 0:
                corner = "top_left"
            elif top == 0 and right == width - 1:
                corner = "top_right"
            elif bottom == height - 1 and right == width - 1:
                corner = "bottom_right"
            elif bottom == height - 1 and left == 0:
                corner = "bottom_left"
            if corner:
                shape = []
                for row, col in component:
                    shape.append((row - top, col - left))
                corner_objects.append((corner, color, shape, bottom - top + 1, right - left + 1))

    for corner, color, shape, object_height, object_width in corner_objects:
        if corner == "top_left":
            target_top, target_left = 0, width - object_width
        elif corner == "top_right":
            target_top, target_left = height - object_height, width - object_width
        elif corner == "bottom_right":
            target_top, target_left = height - object_height, 0
        else:
            target_top, target_left = 0, 0
        for row, col in shape:
            output[target_top + row][target_left + col] = color
    return output
