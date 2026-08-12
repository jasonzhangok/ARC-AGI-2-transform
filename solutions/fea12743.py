def transform(grid):
    height = len(grid)
    width = len(grid[0])
    row_groups = []
    row = 0
    while row < height:
        if any((grid[row][col] != 0 for col in range(width))):
            start = row
            while row + 1 < height and any((grid[row + 1][col] != 0 for col in range(width))):
                row += 1
            row_groups.append((start, row))
        row += 1
    col_groups = []
    col = 0
    while col < width:
        if any((grid[row][col] != 0 for row in range(height))):
            start = col
            while col + 1 < width and any((grid[row][col + 1] != 0 for row in range(height))):
                col += 1
            col_groups.append((start, col))
        col += 1
    tiles = []
    for row_start, row_end in row_groups:
        for col_start, col_end in col_groups:
            points = set()
            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    if grid[row][col] != 0:
                        points.add((row - row_start, col - col_start))
            tiles.append((row_start, col_start, points))
    chosen = None
    for first in range(len(tiles)):
        for second in range(first + 1, len(tiles)):
            if len(tiles[first][2]) != len(tiles[second][2]):
                continue
            for union in range(len(tiles)):
                if union == first or union == second:
                    continue
                if tiles[first][2] != tiles[union][2] and tiles[second][2] != tiles[union][2] and (tiles[first][2] | tiles[second][2] == tiles[union][2]):
                    chosen = (first, second, union)
                    break
            if chosen is not None:
                break
        if chosen is not None:
            break
    output = [row[:] for row in grid]
    if chosen is None:
        output = output
    else:
        for index, color in ((chosen[0], 8), (chosen[1], 8), (chosen[2], 3)):
            row_start, col_start, points = tiles[index]
            for row, col in points:
                output[row_start + row][col_start + col] = color
        output = output
    return output
