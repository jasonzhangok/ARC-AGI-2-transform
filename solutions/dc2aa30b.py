def transform(grid):
    tiles = []
    for block_row in range(3):
        for block_col in range(3):
            tile = [
                grid[block_row * 4 + row][block_col * 4:block_col * 4 + 3]
                for row in range(3)
            ]
            one_count = sum(value == 1 for row in tile for value in row)
            tiles.append((one_count, tile))
    tiles.sort(key=lambda item: item[0])
    ordered_rows = (tiles[6:9], tiles[3:6], tiles[0:3])

    output = [[0] * 11 for _ in range(11)]
    for block_row, tile_row in enumerate(ordered_rows):
        for block_col, (_, tile) in enumerate(tile_row):
            for row in range(3):
                output[block_row * 4 + row][block_col * 4:block_col * 4 + 3] = tile[row]
    return output
