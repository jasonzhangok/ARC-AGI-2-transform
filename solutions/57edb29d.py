def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    panels = []

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == 4 or (start_row, start_col) in seen:
                continue
            cells = []
            queue = [(start_row, start_col)]
            seen.add((start_row, start_col))
            for row, col in queue:
                cells.append((row, col))
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (row + delta_row, col + delta_col)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] != 4
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        queue.append(neighbor)
            panels.append(cells)

    signatures = set()
    marker_color = 0
    target_height = 0
    target_width = 0
    target_color = 0
    for cells in panels:
        top = min(row for row, col in cells)
        bottom = max(row for row, col in cells)
        left = min(col for row, col in cells)
        right = max(col for row, col in cells)
        counts = {}
        for row, col in cells:
            color = grid[row][col]
            counts[color] = counts.get(color, 0) + 1
        base = max(counts, key=counts.get)
        if len(counts) == 1:
            target_height = bottom - top + 1
            target_width = right - left + 1
            target_color = base
        else:
            for row, col in cells:
                if grid[row][col] != base:
                    marker_color = grid[row][col]
                    row_distance = min(row - top, bottom - row)
                    col_distance = min(col - left, right - col)
                    signatures.add((row_distance, col_distance))

    output = [[target_color for col in range(target_width)] for row in range(target_height)]
    for row in range(target_height):
        for col in range(target_width):
            row_distance = min(row, target_height - 1 - row)
            col_distance = min(col, target_width - 1 - col)
            if (row_distance, col_distance) in signatures:
                output[row][col] = marker_color
    return output
