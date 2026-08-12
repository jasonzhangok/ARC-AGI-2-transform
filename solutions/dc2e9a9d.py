def transform(grid):
    """Mirror each marked green frame away from its one-cell marker."""
    height = len(grid)
    width = len(grid[0]) if height else 0
    result = [row[:] for row in grid]
    seen = set()

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 3 or (row, col) in seen:
                continue

            component = []
            pending = [(row, col)]
            seen.add((row, col))
            while pending:
                current_row, current_col = pending.pop()
                component.append((current_row, current_col))
                for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and grid[next_row][next_col] == 3
                            and (next_row, next_col) not in seen):
                        seen.add((next_row, next_col))
                        pending.append((next_row, next_col))

            cells = set(component)
            marker = None
            for current_row, current_col in component:
                neighbors = 0
                for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if (current_row + delta_row, current_col + delta_col) in cells:
                        neighbors += 1
                if neighbors == 1:
                    marker = (current_row, current_col)
                    break

            if marker is None:
                continue

            frame = [cell for cell in component if cell != marker]
            min_row = min(cell[0] for cell in frame)
            max_row = max(cell[0] for cell in frame)
            min_col = min(cell[1] for cell in frame)
            max_col = max(cell[1] for cell in frame)

            if marker[0] < min_row:
                copy_color = 8
                for current_row, current_col in component:
                    new_row = 2 * max_row + 2 - current_row
                    if 0 <= new_row < height:
                        result[new_row][current_col] = copy_color
            elif marker[0] > max_row:
                copy_color = 8
                for current_row, current_col in component:
                    new_row = 2 * min_row - 2 - current_row
                    if 0 <= new_row < height:
                        result[new_row][current_col] = copy_color
            elif marker[1] < min_col:
                copy_color = 1
                for current_row, current_col in component:
                    new_col = 2 * max_col + 2 - current_col
                    if 0 <= new_col < width:
                        result[current_row][new_col] = copy_color
            elif marker[1] > max_col:
                copy_color = 1
                for current_row, current_col in component:
                    new_col = 2 * min_col - 2 - current_col
                    if 0 <= new_col < width:
                        result[current_row][new_col] = copy_color

    return result
