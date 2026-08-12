def transform(grid):
    height = len(grid)
    width = len(grid[0])
    cover = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 3:
                cover.append((row, col))
    cover_top = min(row for row, col in cover)
    cover_bottom = max(row for row, col in cover)
    cover_left = min(col for row, col in cover)
    cover_right = max(col for row, col in cover)

    row_flags = [any(grid[row][col] == 2 for col in range(width)) for row in range(height)]
    col_flags = [any(grid[row][col] == 2 for row in range(height)) for col in range(width)]
    if cover_left == 0 and cover_right == width - 1:
        for row in range(cover_top, cover_bottom + 1):
            row_flags[row] = True
    else:
        for col in range(cover_left, cover_right + 1):
            col_flags[col] = True

    row_bands = []
    row = 0
    while row < height:
        if not row_flags[row]:
            row += 1
            continue
        start = row
        while row + 1 < height and row_flags[row + 1]:
            row += 1
        row_bands.append((start, row))
        row += 1
    col_bands = []
    col = 0
    while col < width:
        if not col_flags[col]:
            col += 1
            continue
        start = col
        while col + 1 < width and col_flags[col + 1]:
            col += 1
        col_bands.append((start, col))
        col += 1

    origins = []
    pattern = []
    for row_start, row_end in row_bands:
        for col_start, col_end in col_bands:
            cells = []
            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    if grid[row][col] == 2:
                        cells.append((row - row_start, col - col_start))
            if cells:
                origins.append((row_start, col_start))
                if not pattern:
                    pattern = cells

    row_starts = [start for start, end in row_bands]
    col_starts = [start for start, end in col_bands]
    if cover_left == 0 and cover_right == width - 1:
        hidden_row_index = row_starts.index(cover_top)
        for row, col in pattern:
            if row == hidden_row_index:
                origins.append((cover_top, col_starts[col]))
    else:
        hidden_col_index = col_starts.index(cover_left)
        for row, col in pattern:
            if col == hidden_col_index:
                origins.append((row_starts[row], cover_left))

    output = [row[:] for row in grid]
    for row, col in cover:
        output[row][col] = 0
    for origin_row, origin_col in origins:
        for row, col in pattern:
            output[origin_row + row][origin_col + col] = 2

    origins.sort()
    for index in range(len(pattern)):
        origin_row, origin_col = origins[index]
        row, col = pattern[index]
        output[origin_row + row][origin_col + col] = 8
    return output
