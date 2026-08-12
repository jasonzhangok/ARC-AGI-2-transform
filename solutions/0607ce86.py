def transform(grid):
    height, width = (len(grid), len(grid[0]))
    best = None
    for start_row in range(4):
        for start_column in range(4):
            for row_gap in range(1, 4):
                for column_gap in range(1, 4):
                    for tile_height in range(3, 8):
                        for tile_width in range(3, 8):
                            for block_rows in range(2, 5):
                                used_height = start_row + block_rows * tile_height + (block_rows - 1) * row_gap
                                if used_height > height:
                                    continue
                                for block_columns in range(2, 5):
                                    if block_rows * block_columns < 6:
                                        continue
                                    used_width = start_column + block_columns * tile_width + (block_columns - 1) * column_gap
                                    if used_width > width:
                                        continue
                                    tile = []
                                    for r in range(tile_height):
                                        tile_row = []
                                        for c in range(tile_width):
                                            samples = [grid[start_row + br * (tile_height + row_gap) + r][start_column + bc * (tile_width + column_gap) + c] for br in range(block_rows) for bc in range(block_columns)]
                                            tile_row.append(max((count_dict := {}) or ([count_dict.update({count_item: count_dict.get(count_item, 0) + 1}) for count_item in samples] and count_dict), key=count_dict.get))
                                        tile.append(tile_row)
                                    if any((value == 0 for row in tile for value in row)):
                                        continue
                                    candidate = [[0] * width for _ in range(height)]
                                    for br in range(block_rows):
                                        for bc in range(block_columns):
                                            for r in range(tile_height):
                                                for c in range(tile_width):
                                                    candidate[start_row + br * (tile_height + row_gap) + r][start_column + bc * (tile_width + column_gap) + c] = tile[r][c]
                                    difference = sum((grid[r][c] != candidate[r][c] for r in range(height) for c in range(width)))
                                    score = (difference, -tile_height * tile_width * block_rows * block_columns)
                                    if best is None or score < best[0]:
                                        best = (score, candidate)
    output = best[1]
    return output
