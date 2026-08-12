def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    seen = set()
    pieces = []
    for column in range(width):
        for row in range(height):
            if grid[row][column] == background or (row, column) in seen:
                continue
            stack = [(row, column)]
            seen.add((row, column))
            cells = []
            while stack:
                current_row, current_column = stack.pop()
                cells.append((current_row, current_column))
                for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_step
                    next_column = current_column + column_step
                    if (0 <= next_row < height and 0 <= next_column < width
                            and (next_row, next_column) not in seen
                            and grid[next_row][next_column] != background):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))
            top = min(cell[0] for cell in cells)
            left = min(cell[1] for cell in cells)
            bottom = max(cell[0] for cell in cells)
            right = max(cell[1] for cell in cells)
            pieces.append((left, top, bottom - top + 1, right - left + 1,
                           grid[row][column]))

    pieces.sort()
    output_width = sum(max(piece[2], piece[3]) for piece in pieces) + len(pieces) - 1
    output = [[background for _ in range(output_width)] for _ in range(10)]

    column = 0
    for _, _, piece_height, piece_width, color in pieces:
        placed_height = min(piece_height, piece_width)
        placed_width = max(piece_height, piece_width)
        for row in range(placed_height):
            for offset in range(placed_width):
                output[row][column + offset] = color
        column += placed_width + 1

    column = 0
    for _, _, piece_height, piece_width, color in pieces:
        placed_height = max(piece_height, piece_width)
        placed_width = min(piece_height, piece_width)
        for row in range(10 - placed_height, 10):
            for offset in range(placed_width):
                output[row][column + offset] = color
        column += placed_width + 1
    return output
