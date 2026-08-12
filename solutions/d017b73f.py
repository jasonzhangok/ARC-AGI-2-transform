def transform(grid):
    height = len(grid)
    width = len(grid[0])

    occupied_columns = [
        column
        for column in range(width)
        if any(grid[row][column] != 0 for row in range(height))
    ]
    runs = []
    for column in occupied_columns:
        if not runs or column != runs[-1][-1] + 1:
            runs.append([column])
        else:
            runs[-1].append(column)

    pieces = []
    for columns in runs:
        left = columns[0]
        cells = {
            (row, column - left): grid[row][column]
            for row in range(height)
            for column in columns
            if grid[row][column] != 0
        }
        pieces.append((len(columns), cells))

    def endpoint_row(cells, side_column):
        candidates = []
        positions = set(cells)
        for row, column in positions:
            if column != side_column:
                continue
            degree = sum(
                (row + dr, column + dc) in positions
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
            )
            if degree <= 1:
                candidates.append(row)
        if len(candidates) != 1:
            raise ValueError("Each piece must have one path endpoint on each side")
        return candidates[0]

    output_width = sum(piece_width for piece_width, _ in pieces)
    output = [[0] * output_width for _ in range(height)]
    output_column = 0
    previous_right_row = None

    for piece_width, cells in pieces:
        left_row = endpoint_row(cells, 0)
        right_row = endpoint_row(cells, piece_width - 1)
        row_shift = 0 if previous_right_row is None else previous_right_row - left_row

        for (row, column), color in cells.items():
            shifted_row = row + row_shift
            if not 0 <= shifted_row < height:
                raise ValueError("Joined path does not fit in the grid height")
            output[shifted_row][output_column + column] = color

        previous_right_row = right_row + row_shift
        output_column += piece_width

    return output
