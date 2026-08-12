def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    five_cells = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 5
    }
    five_top = min(row for row, col in five_cells)
    five_bottom = max(row for row, col in five_cells)
    five_left = min(col for row, col in five_cells)
    five_right = max(col for row, col in five_cells)

    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 0
    }
    components = []
    while remaining:
        first = remaining.pop()
        component = {first}
        frontier = [first]
        while frontier:
            row, col = frontier.pop()
            for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = (row + delta_row, col + delta_col)
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    frontier.append(neighbor)
        components.append(component)

    for component in components:
        if len(component) != 14:
            continue
        core = None
        core_top = core_bottom = core_left = core_right = None
        for core_height, core_width in ((3, 4), (4, 3)):
            for top in range(height - core_height + 1):
                for left in range(width - core_width + 1):
                    rectangle = {
                        (row, col)
                        for row in range(top, top + core_height)
                        for col in range(left, left + core_width)
                    }
                    if rectangle <= component:
                        core = rectangle
                        core_top = top
                        core_bottom = top + core_height - 1
                        core_left = left
                        core_right = left + core_width - 1
        if core is None:
            continue
        vertically_aligned = core_top <= five_bottom and five_top <= core_bottom
        horizontally_separate = core_right < five_left or five_right < core_left
        if not vertically_aligned or not horizontally_separate:
            continue

        for row, col in component - core:
            output[row][col] = 7
        edge_col = core_right if core_right < five_left else core_left
        for row in range(core_top, core_bottom + 1):
            output[row][edge_col] = 6

    return output
