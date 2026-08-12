def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    blocks = []

    for row in range(1, height - 2):
        for col in range(1, width - 2):
            if (grid[row][col] == 2 and grid[row][col + 1] == 2 and
                    grid[row + 1][col] == 2 and grid[row + 1][col + 1] == 2 and
                    not (grid[row - 1][col] == 2 and grid[row - 1][col + 1] == 2) and
                    not (grid[row][col - 1] == 2 and grid[row + 1][col - 1] == 2)):
                blocks.append((row, col))

    rays = []
    for row, col in blocks:
        old_colors = [
            grid[row - 1][col - 1],
            grid[row - 1][col + 2],
            grid[row + 2][col + 2],
            grid[row + 2][col - 1],
        ]
        origins = [
            (row - 1, col - 1),
            (row - 1, col + 2),
            (row + 2, col + 2),
            (row + 2, col - 1),
        ]
        directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        new_colors = [old_colors[3], old_colors[0], old_colors[1], old_colors[2]]
        for origin, direction, color in zip(origins, directions, new_colors):
            rays.append((origin, direction, color))

    for ray_index, ray in enumerate(rays):
        (row, col), (dr, dc), color = ray
        path = []
        while 0 <= row < height and 0 <= col < width and grid[row][col] != 2:
            path.append((row, col))
            row += dr
            col += dc

        contacts = []
        for index, (row, col) in enumerate(path):
            for other_index, other in enumerate(rays):
                (other_row, other_col), _, other_color = other
                if (other_index != ray_index and other_color == color and
                        abs(other_row - row) + abs(other_col - col) == 1):
                    contacts.append(index)
                    break

        limit = len(path)
        if contacts and max(contacts) < len(path) - 1:
            limit = min(contacts) + 1
        for row, col in path[:limit]:
            output[row][col] = color

    return output
