def transform(grid):
    """Slide every four-connected nonzero object rigidly to the right."""
    height = len(grid)
    if height == 0:
        output = []
    else:
        width = len(grid[0])
        seen = set()
        components = []
        for start_row in range(height):
            for start_col in range(width):
                if grid[start_row][start_col] == 0 or (start_row, start_col) in seen:
                    continue
                stack = [(start_row, start_col)]
                seen.add((start_row, start_col))
                component = []
                while stack:
                    row, col = stack.pop()
                    component.append([row, col, grid[row][col]])
                    for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = row + drow
                        next_col = col + dcol
                        if 0 <= next_row < height and 0 <= next_col < width and (grid[next_row][next_col] != 0) and ((next_row, next_col) not in seen):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                components.append(component)
        occupied = {(row, col): index for index, component in enumerate(components) for row, col, _ in component}
        changed = True
        while changed:
            changed = False
            order = [_sort_record_1[2] for _sort_record_1 in sorted(((max((col for _, col, _ in components[_sort_item_1])), -_sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(range(len(components)))), reverse=True)]
            for index in order:
                component = components[index]
                while all((col + 1 < width and occupied.get((row, col + 1), index) == index for row, col, _ in component)):
                    for row, col, _ in component:
                        occupied.pop((row, col), None)
                    for cell in component:
                        cell[1] += 1
                    for row, col, _ in component:
                        occupied[row, col] = index
                    changed = True
        output = [[0 for _ in range(width)] for _ in range(height)]
        for component in components:
            for row, col, color in component:
                output[row][col] = color
        output = output
    return output
