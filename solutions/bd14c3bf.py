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
    classified = []
    for cells in (example,):
        top = min(row for row, _ in cells); bottom = max(row for row, _ in cells)
        left = min(col for _, col in cells); right = max(col for _, col in cells)
        shape = {(row-top,col-left) for row,col in cells}; glyph_height=bottom-top+1; glyph_width=right-left+1
        full_rows={row for row in range(glyph_height) if all((row,col) in shape for col in range(glyph_width))}
        full_cols={col for col in range(glyph_width) if all((row,col) in shape for row in range(glyph_height))}
        strokes=({(row,col) for row in full_rows for col in range(glyph_width)}|{(row,col) for col in full_cols for row in range(glyph_height)})
        glyph_type=None
        if shape==strokes:
            if full_rows=={0,glyph_height-1} and full_cols=={0,glyph_width-1}: glyph_type="frame"
            elif (full_rows=={0,glyph_height-1} and len(full_cols)==1 and next(iter(full_cols)) in (0,glyph_width-1)) or (full_cols=={0,glyph_width-1} and len(full_rows)==1 and next(iter(full_rows)) in (0,glyph_height-1)): glyph_type="three_sides"
            elif (len(full_rows)==1 and 0<next(iter(full_rows))<glyph_height-1 and full_cols=={0,glyph_width-1}) or (len(full_cols)==1 and 0<next(iter(full_cols))<glyph_width-1 and full_rows=={0,glyph_height-1}): glyph_type="h_shape"
        classified.append(glyph_type)
    wanted_type = classified[0]
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
            cells=set(component)
            top=min(r for r,c in cells);bottom=max(r for r,c in cells);left=min(c for r,c in cells);right=max(c for r,c in cells)
            shape={(r-top,c-left) for r,c in cells};glyph_height=bottom-top+1;glyph_width=right-left+1
            full_rows={r for r in range(glyph_height) if all((r,c) in shape for c in range(glyph_width))}
            full_cols={c for c in range(glyph_width) if all((r,c) in shape for r in range(glyph_height))}
            strokes=({(r,c) for r in full_rows for c in range(glyph_width)}|{(r,c) for c in full_cols for r in range(glyph_height)})
            glyph_type=None
            if shape==strokes:
                if full_rows=={0,glyph_height-1} and full_cols=={0,glyph_width-1}:glyph_type="frame"
                elif (full_rows=={0,glyph_height-1} and len(full_cols)==1 and next(iter(full_cols)) in (0,glyph_width-1)) or (full_cols=={0,glyph_width-1} and len(full_rows)==1 and next(iter(full_rows)) in (0,glyph_height-1)):glyph_type="three_sides"
                elif (len(full_rows)==1 and 0<next(iter(full_rows))<glyph_height-1 and full_cols=={0,glyph_width-1}) or (len(full_cols)==1 and 0<next(iter(full_cols))<glyph_width-1 and full_rows=={0,glyph_height-1}):glyph_type="h_shape"
            if glyph_type == wanted_type:
                for comp_row, comp_col in component:
                    output[comp_row][comp_col] = 2
    return output
