def transform(grid):
    height = len(grid)
    width = len(grid[0])
    divider = next(
        col
        for col in range(width)
        if all(grid[row][col] == 5 for row in range(height))
    )

    four_cols = [
        col
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 4
    ]
    if max(four_cols) < divider:
        stencil_left, stencil_right = 0, divider - 1
    else:
        stencil_left, stencil_right = divider + 1, width - 1

    source_cells = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] not in (0, 4, 5)
    ]
    top = min(row for row, _ in source_cells)
    bottom = max(row for row, _ in source_cells)
    left = min(col for _, col in source_cells)
    right = max(col for _, col in source_cells)
    source = [grid[row][left:right + 1] for row in range(top, bottom + 1)]

    row_counts = {}; col_counts = {}
    for row in range(height):
        for col in range(stencil_left, stencil_right + 1):
            if grid[row][col] == 4:
                row_counts[row]=row_counts.get(row,0)+1
                relative=col-stencil_left;col_counts[relative]=col_counts.get(relative,0)+1
    row_separators = sorted(
        row for row, count in row_counts.items() if count == max(row_counts.values())
    )
    col_separators = sorted(
        col for col, count in col_counts.items() if count == max(col_counts.values())
    )

    expanded = []
    for separators,total in ((row_separators,height),(col_separators,stencil_right-stencil_left+1)):
        indices = []
        previous = 0
        for group, separator in enumerate(separators):
            indices.extend([2 * group] * (separator - previous))
            indices.append(2 * group + 1)
            previous = separator + 1
        indices.extend([2 * len(separators)] * (total - previous))
        expanded.append(indices)
    row_indices,col_indices=expanded
    output = [
        [source[source_row][source_col] for source_col in col_indices]
        for source_row in row_indices
    ]
    return output
