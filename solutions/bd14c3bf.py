def _glyph_type(cells):
    top = min(row for row, _ in cells)
    bottom = max(row for row, _ in cells)
    left = min(col for _, col in cells)
    right = max(col for _, col in cells)
    shape = {(row - top, col - left) for row, col in cells}
    height = bottom - top + 1
    width = right - left + 1

    full_rows = {
        row for row in range(height)
        if all((row, col) in shape for col in range(width))
    }
    full_cols = {
        col for col in range(width)
        if all((row, col) in shape for row in range(height))
    }
    strokes = (
        {(row, col) for row in full_rows for col in range(width)}
        | {(row, col) for col in full_cols for row in range(height)}
    )
    if shape != strokes:
        return None

    if full_rows == {0, height - 1} and full_cols == {0, width - 1}:
        return "frame"
    if ((full_rows == {0, height - 1}
         and len(full_cols) == 1
         and next(iter(full_cols)) in (0, width - 1))
            or (full_cols == {0, width - 1}
                and len(full_rows) == 1
                and next(iter(full_rows)) in (0, height - 1))):
        return "three_sides"
    if ((len(full_rows) == 1
         and 0 < next(iter(full_rows)) < height - 1
         and full_cols == {0, width - 1})
            or (len(full_cols) == 1
                and 0 < next(iter(full_cols)) < width - 1
                and full_rows == {0, height - 1})):
        return "h_shape"
    return None


def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    example = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    }
    wanted_type = _glyph_type(example)
    seen = set()

    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                cur_row, cur_col = stack.pop()
                component.append((cur_row, cur_col))
                for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row = cur_row + d_row
                    next_col = cur_col + d_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and (next_row, next_col) not in seen
                            and grid[next_row][next_col] == 1):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            if _glyph_type(set(component)) == wanted_type:
                for comp_row, comp_col in component:
                    output[comp_row][comp_col] = 2
    return output
