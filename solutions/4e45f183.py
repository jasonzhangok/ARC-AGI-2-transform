def transform(grid):
    height = len(grid)
    width = len(grid[0])

    row_groups = []
    row = 0
    while row < height:
        if any(grid[row][col] != 0 for col in range(width)):
            start = row
            while row + 1 < height and any(grid[row + 1][col] != 0 for col in range(width)):
                row += 1
            row_groups.append((start, row))
        row += 1

    col_groups = []
    col = 0
    while col < width:
        if any(grid[row][col] != 0 for row in range(height)):
            start = col
            while col + 1 < width and any(grid[row][col + 1] != 0 for row in range(height)):
                col += 1
            col_groups.append((start, col))
        col += 1

    output = [[0 for col in range(width)] for row in range(height)]
    placed_tiles = {}
    for row_start, row_end in row_groups:
        for col_start, col_end in col_groups:
            tile = []
            counts = {}
            for row in range(row_start, row_end + 1):
                tile_row = []
                for col in range(col_start, col_end + 1):
                    value = grid[row][col]
                    tile_row.append(value)
                    counts[value] = counts.get(value, 0) + 1
                tile.append(tile_row)

            base = tile[0][0]
            for value in counts:
                if counts[value] > counts[base]:
                    base = value
            markers = []
            for local_row in range(len(tile)):
                for local_col in range(len(tile[0])):
                    if tile[local_row][local_col] != base:
                        markers.append((local_row, local_col))

            average_row = sum(point[0] for point in markers) / len(markers)
            average_col = sum(point[1] for point in markers) / len(markers)
            if average_row < 1.5:
                target_row = 0
            elif average_row > 2.5:
                target_row = 2
            else:
                target_row = 1
            if average_col < 1.5:
                target_col = 0
            elif average_col > 2.5:
                target_col = 2
            else:
                target_col = 1
            placed_tiles[(target_row, target_col)] = tile

    for target in placed_tiles:
        target_row, target_col = target
        tile = placed_tiles[target]
        row_start = row_groups[target_row][0]
        col_start = col_groups[target_col][0]
        for local_row in range(len(tile)):
            for local_col in range(len(tile[0])):
                output[row_start + local_row][col_start + local_col] = tile[local_row][local_col]
    return output
