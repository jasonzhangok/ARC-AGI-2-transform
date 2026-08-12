def transform(grid):
    height = len(grid)
    width = len(grid[0])

    separator_rows = []
    for row in range(height):
        if grid[row][0] != 0 and all(grid[row][col] == grid[row][0] for col in range(width)):
            separator_rows.append(row)
    separator_cols = []
    for col in range(width):
        if grid[0][col] != 0 and all(grid[row][col] == grid[0][col] for row in range(height)):
            separator_cols.append(col)

    row_groups = []
    previous = -1
    for separator in separator_rows + [height]:
        if separator > previous + 1:
            row_groups.append((previous + 1, separator - 1))
        previous = separator
    col_groups = []
    previous = -1
    for separator in separator_cols + [width]:
        if separator > previous + 1:
            col_groups.append((previous + 1, separator - 1))
        previous = separator

    tile_rows = len(row_groups)
    tile_cols = len(col_groups)
    tiles = []
    for row_start, row_end in row_groups:
        tile_row = []
        for col_start, col_end in col_groups:
            tile_row.append(grid[row_start][col_start])
        tiles.append(tile_row)

    components = []
    visited = set()
    for start_row in range(tile_rows):
        for start_col in range(tile_cols):
            if tiles[start_row][start_col] == 0 or (start_row, start_col) in visited:
                continue
            component = []
            frontier = [(start_row, start_col)]
            visited.add((start_row, start_col))
            while frontier:
                row, col = frontier.pop()
                component.append((row, col))
                for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (0 <= next_row < tile_rows and 0 <= next_col < tile_cols
                            and tiles[next_row][next_col] != 0
                            and (next_row, next_col) not in visited):
                        visited.add((next_row, next_col))
                        frontier.append((next_row, next_col))
            components.append(component)

    center_color = 0
    for component in components:
        if len(component) == 1:
            row, col = component[0]
            candidate = tiles[row][col]
            appears_in_pattern = False
            for other in components:
                if len(other) > 1:
                    for other_row, other_col in other:
                        if tiles[other_row][other_col] == candidate:
                            appears_in_pattern = True
            if appears_in_pattern:
                center_color = candidate
                break

    exemplar = []
    for component in components:
        contains_center = False
        for row, col in component:
            if tiles[row][col] == center_color:
                contains_center = True
        if contains_center and len(component) > len(exemplar):
            exemplar = component

    center_row = 0
    center_col = 0
    for row, col in exemplar:
        if tiles[row][col] == center_color:
            center_row = row
            center_col = col
            break

    pattern = []
    for row, col in exemplar:
        pattern.append((row - center_row, col - center_col, tiles[row][col]))

    output = [row[:] for row in grid]
    for row in range(tile_rows):
        for col in range(tile_cols):
            if tiles[row][col] == center_color:
                for row_offset, col_offset, color in pattern:
                    target_row = row + row_offset
                    target_col = col + col_offset
                    if 0 <= target_row < tile_rows and 0 <= target_col < tile_cols:
                        for paint_row in range(row_groups[target_row][0], row_groups[target_row][1] + 1):
                            for paint_col in range(col_groups[target_col][0], col_groups[target_col][1] + 1):
                                output[paint_row][paint_col] = color
    return output
