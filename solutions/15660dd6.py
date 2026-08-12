def transform(grid):
    height, width = len(grid), len(grid[0])
    separator = 8
    divider_rows = [r for r in range(height) if all(value == separator for value in grid[r])]
    bands = [(divider_rows[i] + 1, divider_rows[i + 1]) for i in range(len(divider_rows) - 1)]
    probe_top, probe_bottom = bands[0]
    divider_cols = [
        c
        for c in range(1, width)
        if all(grid[r][c] == separator for r in range(probe_top, probe_bottom))
    ]
    panel_ranges = []
    start = 1
    for divider in divider_cols:
        if start < divider:
            panel_ranges.append((start, divider))
        start = divider + 1

    result_panels = []
    for left, right in panel_ranges:
        solid_band = None
        solid_color = None
        template = None
        for top, bottom in bands:
            panel = [row[left:right] for row in grid[top:bottom]]
            interior = [value for row in panel[1:-1] for value in row[1:-1]]
            if interior and len(set(interior)) == 1 and interior[0] not in (1, separator):
                solid_band = (top, bottom)
                solid_color = interior[0]
            elif template is None:
                template = panel
        identifier = grid[solid_band[0]][0]
        result_panels.append([
            [identifier if value == 1 else solid_color if value == 2 else value for value in row]
            for row in template
        ])

    output = []
    for row_index in range(len(result_panels[0])):
        row = []
        for index, panel in enumerate(result_panels):
            if index:
                row.append(separator)
            row.extend(panel[row_index])
        output.append(row)
    return output
