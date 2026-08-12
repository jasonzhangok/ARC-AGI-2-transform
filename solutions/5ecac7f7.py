def transform(grid):
    height = len(grid)
    width = len(grid[0])

    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    background = max(counts, key=counts.get)

    panel_count = (width + 1) // (height + 1)
    output = [[background for col in range(height)] for row in range(height)]

    for panel in range(panel_count):
        panel_left = panel * (height + 1)
        visited = set()
        components = []

        for row in range(height):
            for col in range(height):
                color = grid[row][panel_left + col]
                if color == background or (row, col) in visited:
                    continue

                cells = []
                stack = [(row, col)]
                visited.add((row, col))
                while stack:
                    current_row, current_col = stack.pop()
                    cells.append((current_row, current_col))
                    for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        neighbor_row = current_row + delta_row
                        neighbor_col = current_col + delta_col
                        if not (0 <= neighbor_row < height and 0 <= neighbor_col < height):
                            continue
                        if (neighbor_row, neighbor_col) in visited:
                            continue
                        if grid[neighbor_row][panel_left + neighbor_col] == color:
                            visited.add((neighbor_row, neighbor_col))
                            stack.append((neighbor_row, neighbor_col))

                leftmost = min(col for row, col in cells)
                components.append((leftmost, cells, color))

        components.sort()
        selected_cells = components[panel][1]
        selected_color = components[panel][2]
        for row, col in selected_cells:
            output[row][col] = selected_color

    return output
