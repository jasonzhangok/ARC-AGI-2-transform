def transform(grid):
    height, width = (len(grid), len(grid[0]))
    separator_rows = [r for r, row in enumerate(grid) if all((value == 5 for value in row))]
    separator_cols = [c for c in range(width) if all((grid[r][c] == 5 for r in range(height)))]
    row_cuts = [-1] + separator_rows + [height]
    col_cuts = [-1] + separator_cols + [width]
    row_ranges = [(row_cuts[i] + 1, row_cuts[i + 1]) for i in range(len(row_cuts) - 1)]
    col_ranges = [(col_cuts[i] + 1, col_cuts[i + 1]) for i in range(len(col_cuts) - 1)]
    result = [[5 if r in separator_rows or c in separator_cols else 0 for c in range(width)] for r in range(height)]
    counts = {}
    colors = {}
    for i, (top, bottom) in enumerate(row_ranges):
        for j, (left, right) in enumerate(col_ranges):
            values = [grid[r][c] for r in range(top, bottom) for c in range(left, right) if grid[r][c] not in (0, 5)]
            counts[i, j] = len(values)
            if values:
                colors[i, j] = max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in values] and count_dict), key=count_dict.get)
    maximum = max(counts.values())
    for (i, j), count in counts.items():
        if count == maximum:
            top, bottom = row_ranges[i]
            left, right = col_ranges[j]
            for r in range(top, bottom):
                for c in range(left, right):
                    result[r][c] = colors[i, j]
    output = result
    return output
