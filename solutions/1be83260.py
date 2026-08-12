def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            if value != 0:
                counts[value] = counts.get(value, 0) + 1
    base = None
    for value in counts:
        if base is None or counts[value] > counts[base]:
            base = value
    active_rows = [r for r in range(height) if any(grid[r][c] != 0 for c in range(width))]
    active_cols = [c for c in range(width) if any(grid[r][c] != 0 for r in range(height))]

    bands = []
    for indices in (active_rows, active_cols):
        result = []
        start = previous = indices[0]
        for value in indices[1:]:
            if value != previous + 1:
                result.append((start, previous + 1))
                start = value
            previous = value
        result.append((start, previous + 1))
        bands.append(result)
    row_bands, col_bands = bands
    tile_height = row_bands[0][1] - row_bands[0][0]
    tile_width = col_bands[0][1] - col_bands[0][0]
    instruction = next(
        (top, left)
        for top, bottom in row_bands
        for left, right in col_bands
        if any(grid[r][c] not in (0, base) for r in range(top, bottom) for c in range(left, right))
    )
    top, left = instruction
    code = [
        [grid[top + r][left + c] for c in range(1, tile_width, 2)]
        for r in range(1, tile_height, 2)
    ]
    base_tile = [
        [grid[row_bands[0][0] + r][col_bands[0][0] + c] == base for c in range(tile_width)]
        for r in range(tile_height)
    ]
    out_height = len(code) * tile_height + len(code) - 1
    out_width = len(code[0]) * tile_width + len(code[0]) - 1
    output = [[base] * out_width for _ in range(out_height)]
    for code_row, values in enumerate(code):
        for code_col, color in enumerate(values):
            origin_row = code_row * (tile_height + 1)
            origin_col = code_col * (tile_width + 1)
            for r in range(tile_height):
                for c in range(tile_width):
                    if base_tile[r][c]:
                        output[origin_row + r][origin_col + c] = color
    return output
