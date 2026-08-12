def transform(grid):
    height = len(grid)
    width = len(grid[0])
    seen = set()
    pieces = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 0 or (row, column) in seen:
                continue
            color = grid[row][column]
            cells = [(row, column)]
            seen.add((row, column))
            cursor = 0
            while cursor < len(cells):
                current_row, current_column = cells[cursor]
                cursor += 1
                for next_row, next_column in ((current_row - 1, current_column),
                                                (current_row + 1, current_column),
                                                (current_row, current_column - 1),
                                                (current_row, current_column + 1)):
                    if (0 <= next_row < height and 0 <= next_column < width
                            and grid[next_row][next_column] == color
                            and (next_row, next_column) not in seen):
                        seen.add((next_row, next_column))
                        cells.append((next_row, next_column))
            minimum_row = min(cell_row for cell_row, cell_column in cells)
            minimum_column = min(cell_column for cell_row, cell_column in cells)
            normalized = set((cell_row - minimum_row, cell_column - minimum_column)
                             for cell_row, cell_column in cells)
            pieces.append((color, normalized, minimum_row, minimum_column))

    for index in range(1, len(pieces)):
        piece = pieces[index]
        position = index
        while position > 0:
            previous = pieces[position - 1]
            piece_precedes = (len(piece[1]) > len(previous[1])
                              or (len(piece[1]) == len(previous[1])
                                  and (piece[2], piece[3]) > (previous[2], previous[3])))
            if not piece_precedes:
                break
            pieces[position] = previous
            position -= 1
        pieces[position] = piece

    piece_options = []
    for color, cells, source_row, source_column in pieces:
        variants = []
        current = set(cells)
        for rotation in range(4):
            poses = [current, set((cell_row, -cell_column)
                                  for cell_row, cell_column in current)]
            for pose in poses:
                minimum_row = min(cell_row for cell_row, cell_column in pose)
                minimum_column = min(cell_column for cell_row, cell_column in pose)
                normalized = frozenset((cell_row - minimum_row, cell_column - minimum_column)
                                       for cell_row, cell_column in pose)
                if normalized not in variants:
                    variants.append(normalized)
            current = set((cell_column, -cell_row) for cell_row, cell_column in current)
        options = []
        for pose in variants:
            pose_height = max(cell_row for cell_row, cell_column in pose) + 1
            pose_width = max(cell_column for cell_row, cell_column in pose) + 1
            for top in range(4 - pose_height):
                for left in range(5 - pose_width):
                    options.append((color, [(top + cell_row, left + cell_column)
                                            for cell_row, cell_column in pose]))
        piece_options.append(options)

    blank = [[0 for column in range(4)] for row in range(3)]
    states = [(0, blank)]
    output = []
    while states:
        piece_index, canvas = states.pop()
        if piece_index == len(piece_options):
            if all(canvas[row][column] != 0 for row in range(3) for column in range(4)):
                output = canvas
                break
            continue
        next_states = []
        for color, target in piece_options[piece_index]:
            if all(canvas[row][column] == 0 for row, column in target):
                next_canvas = [row[:] for row in canvas]
                for row, column in target:
                    next_canvas[row][column] = color
                next_states.append((piece_index + 1, next_canvas))
        for state in reversed(next_states):
            states.append(state)
    return output
