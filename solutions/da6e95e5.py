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

    best_size = 0
    best_box = None
    colors = list(counts)
    colors.sort()
    for size in range(2, min(h, w) // 2 + 1):
        for color in colors:
            if color == background:
                continue
            top_left = []
            top_right = []
            bottom_left = []
            bottom_right = []
            for r in range(h - size + 1):
                for c in range(w - size + 1):
                    tl = True
                    tr = True
                    bl = True
                    br = True
                    for offset in range(size):
                        if grid[r][c + offset] != color or grid[r + offset][c] != color:
                            tl = False
                        if grid[r][c + offset] != color or grid[r + offset][c + size - 1] != color:
                            tr = False
                        if grid[r + size - 1][c + offset] != color or grid[r + offset][c] != color:
                            bl = False
                        if grid[r + size - 1][c + offset] != color or grid[r + offset][c + size - 1] != color:
                            br = False
                    for inner_r in range(1, size):
                        for inner_c in range(1, size):
                            if (inner_r != size - 1 or inner_c != size - 1) and grid[r + inner_r][c + inner_c] == color:
                                tl = False
                    for inner_r in range(1, size):
                        for inner_c in range(size - 1):
                            if (inner_r != size - 1 or inner_c != 0) and grid[r + inner_r][c + inner_c] == color:
                                tr = False
                    for inner_r in range(size - 1):
                        for inner_c in range(1, size):
                            if (inner_r != 0 or inner_c != size - 1) and grid[r + inner_r][c + inner_c] == color:
                                bl = False
                    for inner_r in range(size - 1):
                        for inner_c in range(size - 1):
                            if (inner_r != 0 or inner_c != 0) and grid[r + inner_r][c + inner_c] == color:
                                br = False
                    if tl:
                        top_left.append((r, c))
                    if tr:
                        top_right.append((r, c))
                    if bl:
                        bottom_left.append((r, c))
                    if br:
                        bottom_right.append((r, c))

            bottom_right_set = set(bottom_right)
            for top, left in top_left:
                for other_top, right_square in top_right:
                    if other_top != top or right_square < left + size:
                        continue
                    for bottom_square, other_left in bottom_left:
                        if other_left != left or bottom_square < top + size:
                            continue
                        if (bottom_square, right_square) not in bottom_right_set:
                            continue
                        arms = set()
                        for offset in range(size):
                            arms.add((top, left + offset))
                            arms.add((top + offset, left))
                            arms.add((top, right_square + offset))
                            arms.add((top + offset, right_square + size - 1))
                            arms.add((bottom_square + size - 1, left + offset))
                            arms.add((bottom_square + offset, left))
                            arms.add((bottom_square + size - 1, right_square + offset))
                            arms.add((bottom_square + offset, right_square + size - 1))

                        motif = []
                        valid = True
                        for r in range(top, bottom_square + size):
                            for c in range(left, right_square + size):
                                if (r, c) in arms or grid[r][c] == background:
                                    continue
                                if grid[r][c] != color:
                                    valid = False
                                motif.append((r, c))
                        if valid and motif and size > best_size:
                            motif_top = motif[0][0]
                            motif_bottom = motif[0][0]
                            motif_left = motif[0][1]
                            motif_right = motif[0][1]
                            for r, c in motif:
                                if r < motif_top:
                                    motif_top = r
                                if r > motif_bottom:
                                    motif_bottom = r
                                if c < motif_left:
                                    motif_left = c
                                if c > motif_right:
                                    motif_right = c
                            best_size = size
                            best_box = (motif_top, motif_left, motif_bottom, motif_right)

    if best_box is None:
        return [row[:] for row in grid]
    top, left, bottom, right = best_box
    output = []
    for r in range(top, bottom + 1):
        output.append(grid[r][left:right + 1])
    return output
