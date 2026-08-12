

def transform(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    components = []
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 0 or (start_row, start_col) in seen:
                continue
            component = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                component.append((row, col, grid[row][col]))
                for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row, next_col = row + drow, col + dcol
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and grid[next_row][next_col] != 0
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))
            components.append(component)

    for component in components:
        fours = [(row, col) for row, col, value in component if value == 4]
        if not fours:
            continue
        row_counts = {}
        for cell_value in (row for row, _ in fours):
            row_counts[cell_value] = row_counts.get(cell_value, 0) + 1
        col_counts = {}
        for cell_value in (col for _, col in fours):
            col_counts[cell_value] = col_counts.get(cell_value, 0) + 1
        horizontal = max(row_counts.values()) >= max(col_counts.values())
        axis = (
            max(row_counts, key=row_counts.get)
            if horizontal
            else max(col_counts, key=col_counts.get)
        )
        markers = [
            (row, col)
            for row, col in fours
            if (row if horizontal else col) != axis
        ]
        if not markers:
            continue
        marker_position = markers[0][0] if horizontal else markers[0][1]
        source_sign = 1 if marker_position > axis else -1

        for row, col, _ in component:
            position = row if horizontal else col
            if (position - axis) * source_sign < 0:
                output[row][col] = 0
        for row, col, value in component:
            position = row if horizontal else col
            if (position - axis) * source_sign <= 0:
                continue
            target_row, target_col = (
                (2 * axis - row, col)
                if horizontal
                else (row, 2 * axis - col)
            )
            if 0 <= target_row < height and 0 <= target_col < width:
                output[target_row][target_col] = value
    return output
