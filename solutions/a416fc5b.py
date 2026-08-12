def transform(grid):
    """Complete the panel cycle, or clear an already completed state."""
    height = len(grid)
    width = len(grid[0]) if height else 0
    if not height:
        return []

    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    separator_rows = [
        row
        for row in range(height)
        if len(set(grid[row])) == 1 and grid[row][0] != background
    ]
    separator_cols = [
        col
        for col in range(width)
        if len({grid[row][col] for row in range(height)}) == 1
        and grid[0][col] != background
    ]

    row_ranges = []
    start = 0
    for boundary in separator_rows + [height]:
        if start < boundary:
            row_ranges.append((start, boundary))
        start = boundary + 1
    col_ranges = []
    start = 0
    for boundary in separator_cols + [width]:
        if start < boundary:
            col_ranges.append((start, boundary))
        start = boundary + 1

    panels = {}
    motif = []
    motif_cell_count = 0
    for panel_row, (top, bottom) in enumerate(row_ranges):
        for panel_col, (left, right) in enumerate(col_ranges):
            cells = []
            colors = set()
            for row in range(top, bottom):
                for col in range(left, right):
                    if grid[row][col] != background:
                        cells.append((row - top, col - left))
                        colors.add(grid[row][col])
            if colors:
                color = next(iter(colors))
                panels[(panel_row, panel_col)] = color
                motif_cell_count += len(cells)
                if color == 2 and not motif:
                    motif = cells

    panel_colors = set(panels.values())
    if 5 in panel_colors and 8 in panel_colors:
        new_height = motif_cell_count
        new_width = motif_cell_count
        return [
            [background for _ in range(new_width)]
            for _ in range(new_height)
        ]

    twos = [position for position, color in panels.items() if color == 2]
    center = next(
        position
        for position in twos
        if position == (len(row_ranges) // 2, len(col_ranges) // 2)
    )
    other = next(position for position in twos if position != center)
    opposite = (2 * center[0] - other[0], 2 * center[1] - other[1])
    perimeter = [
        (0, 0), (0, 1), (0, 2), (1, 2),
        (2, 2), (2, 1), (2, 0), (1, 0),
    ]
    index = perimeter.index(opposite)
    additions = {
        perimeter[(index + 1) % len(perimeter)]: 8,
        perimeter[(index - 1) % len(perimeter)]: 5,
    }

    output = [row[:] for row in grid]
    for (panel_row, panel_col), color in additions.items():
        top, _ = row_ranges[panel_row]
        left, _ = col_ranges[panel_col]
        for delta_row, delta_col in motif:
            output[top + delta_row][left + delta_col] = color
    return output
