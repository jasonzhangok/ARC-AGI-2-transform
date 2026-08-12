def transform(grid):
    try:
        if not grid or not grid[0]:
            raise StopIteration([])
        height = len(grid)
        width = len(grid[0])
        seen = set()
        components = []
        for start_row in range(height):
            for start_col in range(width):
                if grid[start_row][start_col] == 0 or (start_row, start_col) in seen:
                    continue
                stack = [(start_row, start_col)]
                seen.add((start_row, start_col))
                component = []
                while stack:
                    row, col = stack.pop()
                    component.append((row, col))
                    for drow, dcol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = row + drow
                        next_col = col + dcol
                        if 0 <= next_row < height and 0 <= next_col < width and (grid[next_row][next_col] != 0) and ((next_row, next_col) not in seen):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                components.append(component)
        canvas_components = [comp for comp in components if len(comp) == ((min((r for r, _ in comp)), max((r for r, _ in comp)), min((c for _, c in comp)), max((c for _, c in comp)))[1] - (min((r for r, _ in comp)), max((r for r, _ in comp)), min((c for _, c in comp)), max((c for _, c in comp)))[0] + 1) * ((min((r for r, _ in comp)), max((r for r, _ in comp)), min((c for _, c in comp)), max((c for _, c in comp)))[3] - (min((r for r, _ in comp)), max((r for r, _ in comp)), min((c for _, c in comp)), max((c for _, c in comp)))[2] + 1) and len({grid[r][c] for r, c in comp}) == 1]
        if len(canvas_components) != 1:
            raise StopIteration([])
        canvas_component = canvas_components[0]
        base_color = grid[canvas_component[0][0]][canvas_component[0][1]]
        small_components = [comp for comp in components if comp is not canvas_component]
        layout_components = [comp for comp in small_components if base_color in {grid[r][c] for r, c in comp} and 8 in {grid[r][c] for r, c in comp} and (len({grid[r][c] for r, c in comp}) == 2)]
        if len(layout_components) != 1:
            raise StopIteration([])
        layout_component = layout_components[0]
        stamp_components = [comp for comp in small_components if comp is not layout_component]
        if len(stamp_components) != 1:
            raise StopIteration([])
        stamp_component = stamp_components[0]
        canvas_top, canvas_bottom, canvas_left, canvas_right = (min((r for r, _ in canvas_component)), max((r for r, _ in canvas_component)), min((c for _, c in canvas_component)), max((c for _, c in canvas_component)))
        stamp_top, stamp_bottom, stamp_left, stamp_right = (min((r for r, _ in stamp_component)), max((r for r, _ in stamp_component)), min((c for _, c in stamp_component)), max((c for _, c in stamp_component)))
        layout_top, layout_bottom, layout_left, layout_right = (min((r for r, _ in layout_component)), max((r for r, _ in layout_component)), min((c for _, c in layout_component)), max((c for _, c in layout_component)))
        output_height = canvas_bottom - canvas_top + 1
        output_width = canvas_right - canvas_left + 1
        stamp_height = stamp_bottom - stamp_top + 1
        stamp_width = stamp_right - stamp_left + 1
        if output_height % stamp_height or output_width % stamp_width:
            raise StopIteration([])
        layout_height = output_height // stamp_height
        layout_width = output_width // stamp_width
        layout_pixel_height = layout_bottom - layout_top + 1
        layout_pixel_width = layout_right - layout_left + 1
        if layout_pixel_height % layout_height or layout_pixel_width % layout_width:
            raise StopIteration([])
        row_scale = layout_pixel_height // layout_height
        col_scale = layout_pixel_width // layout_width
        if row_scale != col_scale:
            raise StopIteration([])
        output = [[base_color for _ in range(output_width)] for _ in range(output_height)]
        for layout_row in range(layout_height):
            for layout_col in range(layout_width):
                source_row = layout_top + layout_row * row_scale
                source_col = layout_left + layout_col * col_scale
                if grid[source_row][source_col] != 8:
                    continue
                for stamp_row in range(stamp_height):
                    for stamp_col in range(stamp_width):
                        if grid[stamp_top + stamp_row][stamp_left + stamp_col] == 8:
                            output[layout_row * stamp_height + stamp_row][layout_col * stamp_width + stamp_col] = 8
        raise StopIteration(output)
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
