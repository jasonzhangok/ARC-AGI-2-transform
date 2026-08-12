def transform(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            component = []
            stack = [(row, col)]
            seen.add((row, col))
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_step
                    next_col = current_col + col_step
                    next_cell = (next_row, next_col)
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and next_cell not in seen
                        and grid[next_row][next_col] != 0
                    ):
                        seen.add(next_cell)
                        stack.append(next_cell)
            components.append(component)

    selected = max(
        components,
        key=lambda component: sum(grid[row][col] == 2 for row, col in component),
    )
    top = min(row for row, _ in selected)
    bottom = max(row for row, _ in selected)
    left = min(col for _, col in selected)
    right = max(col for _, col in selected)
    return [grid[row][left:right + 1] for row in range(top, bottom + 1)]
