def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    panels = []
    seen = set()
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color == background or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor_row = current_row + row_step
                    neighbor_col = current_col + col_step
                    neighbor = (neighbor_row, neighbor_col)
                    if (0 <= neighbor_row < height and 0 <= neighbor_col < width
                            and grid[neighbor_row][neighbor_col] == color
                            and neighbor not in seen):
                        seen.add(neighbor)
                        stack.append(neighbor)
            top = min(cell[0] for cell in cells)
            bottom = max(cell[0] for cell in cells)
            left = min(cell[1] for cell in cells)
            right = max(cell[1] for cell in cells)
            area = (bottom - top + 1) * (right - left + 1)
            if len(cells) >= 20 and len(cells) * 10 >= area * 7:
                panels.append((top, bottom, left, right, color))

    anomalies = []
    anomaly_counts = {}
    for panel_index, panel in enumerate(panels):
        top, bottom, left, right, panel_color = panel
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if grid[row][col] != panel_color:
                    value = grid[row][col]
                    anomalies.append((value, row, col, panel_index))
                    anomaly_counts[value] = anomaly_counts.get(value, 0) + 1
    marker_color = max(anomaly_counts, key=anomaly_counts.get)

    legend = []
    for row in range(height):
        for col in range(width):
            inside_panel = False
            for top, bottom, left, right, panel_color in panels:
                if top <= row <= bottom and left <= col <= right:
                    inside_panel = True
                    break
            if not inside_panel and grid[row][col] != background:
                legend.append((row, col, grid[row][col]))

    legend_top = min(row for row, col, value in legend)
    legend_bottom = max(row for row, col, value in legend)
    legend_left = min(col for row, col, value in legend)
    legend_right = max(col for row, col, value in legend)
    reference_row = (legend_top + legend_bottom) // 2
    reference_col = (legend_left + legend_right) // 2

    horizontal_color = None
    if (reference_col - 2 >= 0 and reference_col + 2 < width
            and grid[reference_row][reference_col - 2]
            == grid[reference_row][reference_col - 1]
            == grid[reference_row][reference_col + 1]
            == grid[reference_row][reference_col + 2]
            != background):
        horizontal_color = grid[reference_row][reference_col - 1]
    vertical_color = None
    if (reference_row - 2 >= 0 and reference_row + 2 < height
            and grid[reference_row - 2][reference_col]
            == grid[reference_row - 1][reference_col]
            == grid[reference_row + 1][reference_col]
            == grid[reference_row + 2][reference_col]
            != background):
        vertical_color = grid[reference_row - 1][reference_col]

    output = [row[:] for row in grid]
    for row, col, value in legend:
        output[row][col] = background

    for panel_index, panel in enumerate(panels):
        top, bottom, left, right, panel_color = panel
        markers = []
        for value, row, col, anomaly_panel in anomalies:
            if value == marker_color and anomaly_panel == panel_index:
                markers.append((row, col))
        for marker_row, marker_col in markers:
            if horizontal_color is not None:
                for col in range(left, right + 1):
                    output[marker_row][col] = horizontal_color
            if vertical_color is not None:
                for row in range(top, bottom + 1):
                    output[row][marker_col] = vertical_color
            for legend_row, legend_col, value in legend:
                row = marker_row + legend_row - reference_row
                col = marker_col + legend_col - reference_col
                if top <= row <= bottom and left <= col <= right:
                    output[row][col] = value
    return output
