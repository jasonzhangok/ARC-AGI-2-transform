def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 7:
                colors.add(grid[row][col])

    target_cavity = []
    filler_color = 7
    for container_color in colors:
        remaining = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] == container_color:
                    remaining.add((row, col))
        components = []
        while remaining:
            start = remaining.pop()
            component = {start}
            stack = [start]
            while stack:
                row, col = stack.pop()
                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        neighbor = (row + row_offset, col + col_offset)
                        if neighbor in remaining:
                            remaining.remove(neighbor)
                            component.add(neighbor)
                            stack.append(neighbor)
            components.append(component)

        for component in components:
            cavity = []
            top = min(row for row, col in component)
            bottom = max(row for row, col in component)
            for row in range(top, bottom + 1):
                columns = [col for cell_row, col in component if cell_row == row]
                if len(columns) >= 2:
                    for col in range(min(columns) + 1, max(columns)):
                        if grid[row][col] == 7:
                            cavity.append((row, col))
            if not cavity:
                continue
            for candidate_color in colors:
                if candidate_color == container_color:
                    continue
                candidate_count = 0
                for row in range(height):
                    for col in range(width):
                        if grid[row][col] == candidate_color:
                            candidate_count += 1
                if candidate_count == len(cavity):
                    target_cavity = cavity
                    filler_color = candidate_color

    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if output[row][col] == filler_color:
                output[row][col] = 7
    for row, col in target_cavity:
        output[row][col] = filler_color
    return output
