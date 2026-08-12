def transform(grid):
    h = len(grid)
    w = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = 0
    largest = -1
    for value in counts:
        if counts[value] > largest:
            largest = counts[value]
            background = value

    moves = []
    for r in range(1, h - 1):
        clear_to_right = True
        for c in range(2, w):
            if grid[r][c] != 0:
                clear_to_right = False
                break
        if clear_to_right:
            tile = []
            for rr in range(r - 1, r + 2):
                tile.append(grid[rr][0:3])
            tile_is_valid = True
            for c in range(3):
                if tile[0][c] != 0 or tile[2][c] != 0:
                    tile_is_valid = False
            if tile[1][0] == 0 and tile[1][1] == 0:
                tile_is_valid = False
            if tile_is_valid:
                moves.append((0, r, 0, w - 3, tile))
        else:
            clear_to_left = True
            for c in range(w - 2):
                if grid[r][c] != 0:
                    clear_to_left = False
                    break
            if clear_to_left:
                tile = []
                for rr in range(r - 1, r + 2):
                    tile.append(grid[rr][w - 3:w])
                tile_is_valid = True
                for c in range(3):
                    if tile[0][c] != 0 or tile[2][c] != 0:
                        tile_is_valid = False
                if tile[1][1] == 0 and tile[1][2] == 0:
                    tile_is_valid = False
                if tile_is_valid:
                    moves.append((0, r, w - 3, 0, tile))

    for c in range(1, w - 1):
        clear_to_bottom = True
        for r in range(2, h):
            if grid[r][c] != 0:
                clear_to_bottom = False
                break
        if clear_to_bottom:
            tile = []
            for rr in range(3):
                tile.append(grid[rr][c - 1:c + 2])
            tile_is_valid = True
            for r in range(3):
                if tile[r][0] != 0 or tile[r][2] != 0:
                    tile_is_valid = False
            if tile[0][1] == 0 and tile[1][1] == 0:
                tile_is_valid = False
            if tile_is_valid:
                moves.append((1, c, 0, h - 3, tile))
        else:
            clear_to_top = True
            for r in range(h - 2):
                if grid[r][c] != 0:
                    clear_to_top = False
                    break
            if clear_to_top:
                tile = []
                for rr in range(h - 3, h):
                    tile.append(grid[rr][c - 1:c + 2])
                tile_is_valid = True
                for r in range(3):
                    if tile[r][0] != 0 or tile[r][2] != 0:
                        tile_is_valid = False
                if tile[1][1] == 0 and tile[2][1] == 0:
                    tile_is_valid = False
                if tile_is_valid:
                    moves.append((1, c, h - 3, 0, tile))

    output = [row[:] for row in grid]
    for axis, middle, source, target, tile in moves:
        if axis == 0:
            for c in range(w):
                output[middle][c] = background
            for r in range(middle - 1, middle + 2):
                for c in range(source, source + 3):
                    output[r][c] = background
        else:
            for r in range(h):
                output[r][middle] = background
            for r in range(source, source + 3):
                for c in range(middle - 1, middle + 2):
                    output[r][c] = background
    for axis, middle, source, target, tile in moves:
        if axis == 0:
            for r in range(3):
                for c in range(3):
                    output[middle - 1 + r][target + c] = tile[r][c]
        else:
            for r in range(3):
                for c in range(3):
                    output[target + r][middle - 1 + c] = tile[r][c]
    return output
