def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] != 5 or (start_row, start_col) in seen:
                continue
            component = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                component.append((row, col))
                for drow in (-1, 0, 1):
                    for dcol in (-1, 0, 1):
                        next_row, next_col = row + drow, col + dcol
                        if (
                            (drow != 0 or dcol != 0)
                            and 0 <= next_row < height
                            and 0 <= next_col < width
                            and grid[next_row][next_col] == 5
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            queue.append((next_row, next_col))
            cells = set(component)
            has_diagonal_three = any(
                (row + drow, col + dcol) in cells
                and (row + 2 * drow, col + 2 * dcol) in cells
                for row, col in component
                for drow, dcol in ((1, 1), (1, -1))
            )
            if has_diagonal_three:
                for row, col in component:
                    output[row][col] = 8
    return output
