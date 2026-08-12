from collections import Counter


def transform(grid):
    height, width = len(grid), len(grid[0])
    separator = Counter(value for row in grid for value in row if value != 0).most_common(1)[0][0]
    pattern = set()
    for tile_row in (0, 6, 12):
        for tile_col in (0, 6, 12):
            for row in range(5):
                for col in range(5):
                    if grid[tile_row + row][tile_col + col] not in (0, separator):
                        pattern.add((row, col))
    output = [row[:] for row in grid]
    for tile_row in (0, 6, 12):
        for tile_col in (0, 6, 12):
            for row, col in pattern:
                if output[tile_row + row][tile_col + col] == 0:
                    output[tile_row + row][tile_col + col] = separator
    return output
