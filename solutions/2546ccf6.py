from collections import defaultdict


def transform(grid):
    height, width = len(grid), len(grid[0])
    separator = next(
        value
        for value in set(value for row in grid for value in row)
        if any(all(cell == value for cell in row) for row in grid)
    )
    separator_rows = [r for r, row in enumerate(grid) if all(v == separator for v in row)]
    separator_columns = [
        c for c in range(width) if all(grid[r][c] == separator for r in range(height))
    ]
    row_bounds = [-1] + separator_rows + [height]
    column_bounds = [-1] + separator_columns + [width]
    row_ranges = [range(row_bounds[i] + 1, row_bounds[i + 1]) for i in range(len(row_bounds) - 1)]
    column_ranges = [
        range(column_bounds[i] + 1, column_bounds[i + 1])
        for i in range(len(column_bounds) - 1)
    ]

    panels_by_color = defaultdict(list)
    for panel_row, rows in enumerate(row_ranges):
        for panel_column, columns in enumerate(column_ranges):
            colors = {
                grid[r][c]
                for r in rows
                for c in columns
                if grid[r][c] not in (0, separator)
            }
            for color in colors:
                panels_by_color[color].append((panel_row, panel_column))

    result = [row[:] for row in grid]
    for color, occupied in panels_by_color.items():
        panel_rows = sorted({r for r, _ in occupied})
        panel_columns = sorted({c for _, c in occupied})
        if len(occupied) != 3 or len(panel_rows) != 2 or len(panel_columns) != 2:
            continue
        missing = next(
            (r, c)
            for r in panel_rows
            for c in panel_columns
            if (r, c) not in occupied
        )
        opposite = (
            panel_rows[1] if missing[0] == panel_rows[0] else panel_rows[0],
            panel_columns[1] if missing[1] == panel_columns[0] else panel_columns[0],
        )
        source_rows = list(row_ranges[opposite[0]])
        source_columns = list(column_ranges[opposite[1]])
        target_rows = list(row_ranges[missing[0]])
        target_columns = list(column_ranges[missing[1]])
        for target_r, source_r in zip(target_rows, reversed(source_rows)):
            for target_c, source_c in zip(target_columns, reversed(source_columns)):
                result[target_r][target_c] = grid[source_r][source_c]
    return result
