def transform(grid):
    height, width = (len(grid), len(grid[0]))
    seen = set()
    crops = []
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
                    if 0 <= next_row < height and 0 <= next_col < width and (next_cell not in seen) and (grid[next_row][next_col] != 0):
                        seen.add(next_cell)
                        stack.append(next_cell)
            top = min((current_row for current_row, _ in component))
            bottom = max((current_row for current_row, _ in component))
            left = min((current_col for _, current_col in component))
            right = max((current_col for _, current_col in component))
            crops.append(tuple((tuple(grid[r][left:right + 1]) for r in range(top, bottom + 1))))
    counts = {}
    for cell_value in crops:
        counts[cell_value] = counts.get(cell_value, 0) + 1
    repeated = next((crop for crop, amount in counts.items() if amount > 1))
    output = [list(row) for row in repeated]
    return output
