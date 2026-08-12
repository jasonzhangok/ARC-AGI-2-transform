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

    template = max(
        (component for component in components if any(v == 1 for _, _, v in component)),
        key=len,
    )
    template_cells = {(row, col) for row, col, _ in template}
    anchors = sorted((row, col) for row, col, value in template if value == 2)
    pattern = [(row, col) for row, col, value in template if value == 1]

    markers = []
    for component in components:
        if any((row, col) in template_cells for row, col, _ in component):
            continue
        if any(value != 2 for _, _, value in component):
            continue
        rows = [row for row, _, _ in component]
        cols = [col for _, col, _ in component]
        scale = max(max(rows) - min(rows) + 1, max(cols) - min(cols) + 1)
        markers.append((min(rows), min(cols), scale))

    for marker_row, marker_col, scale in markers:
        marker_positions = {
            (row, col) for row, col, marker_scale in markers if marker_scale == scale
        }
        for anchor_row, anchor_col in anchors:
            base_row = marker_row - anchor_row * scale
            base_col = marker_col - anchor_col * scale
            expected = {
                (base_row + row * scale, base_col + col * scale)
                for row, col in anchors
            }
            if not expected <= marker_positions:
                continue
            for row, col in pattern:
                for out_row in range(base_row + row * scale, base_row + (row + 1) * scale):
                    for out_col in range(base_col + col * scale, base_col + (col + 1) * scale):
                        if 0 <= out_row < height and 0 <= out_col < width:
                            output[out_row][out_col] = 1
            break

    return output
