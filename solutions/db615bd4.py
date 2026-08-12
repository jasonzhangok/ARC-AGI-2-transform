def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = {}; order = []
    for source_row in grid:
        for value in source_row:
            if value not in counts: counts[value] = 0; order.append(value)
            counts[value] += 1
    ranked = sorted((-counts[color], index, color) for index, color in enumerate(order))
    background, lattice = ranked[0][2], ranked[1][2]

    positions = {
        color: {
            (row, col)
            for row in range(height)
            for col in range(width)
            if grid[row][col] == color
        }
        for color in counts
        if color not in (background, lattice)
    }
    frames = []
    for color, points in positions.items():
        frame_top=min(row for row,_ in points);frame_bottom=max(row for row,_ in points)
        frame_left=min(col for _,col in points);frame_right=max(col for _,col in points)
        box=None
        if frame_top!=frame_bottom and frame_left!=frame_right:
            frame_rows=range(frame_top,frame_bottom+1,2);frame_cols=range(frame_left,frame_right+1,2)
            expected=({(frame_top,col) for col in frame_cols}|{(frame_bottom,col) for col in frame_cols}|{(row,frame_left) for row in frame_rows}|{(row,frame_right) for row in frame_rows})
            if points==expected:box=(frame_top,frame_left,frame_bottom,frame_right)
        if box is not None:frames.append((box,color))
    (top,left,bottom,right),frame_color=max((((item[0][2]-item[0][0])*(item[0][3]-item[0][1]),-index,item) for index,item in enumerate(frames)))[2]

    pieces = []
    ignored={background,lattice,frame_color}
    remaining={(row,col) for row in range(height) for col in range(width) if grid[row][col] not in ignored}
    sampled_components=[]
    while remaining:
        start=remaining.pop();color=grid[start[0]][start[1]];stack=[start];points={start}
        while stack:
            component_row,component_col=stack.pop()
            for dr,dc in ((-2,0),(2,0),(0,-2),(0,2)):
                point=component_row+dr,component_col+dc
                if point in remaining and grid[point[0]][point[1]]==color:
                    remaining.remove(point);points.add(point);stack.append(point)
        sampled_components.append((color,points))
    for color, points in sampled_components:
        piece_top = min(row for row, _ in points)
        piece_bottom = max(row for row, _ in points)
        piece_left = min(col for _, col in points)
        piece_right = max(col for _, col in points)
        pieces.append(
            {
                "color": color,
                "height": piece_bottom - piece_top + 1,
                "width": piece_right - piece_left + 1,
                "center_row": piece_top + piece_bottom,
                "center_col": piece_left + piece_right,
                "points": points,
            }
        )

    output = [row[:] for row in grid]
    for piece in pieces:
        for row, col in piece["points"]:
            output[row][col] = background

    for row in range(top + 1, bottom):
        for col in range(left + 1, right):
            output[row][col] = background

    for col in range(left, right + 1):
        output[top][col] = frame_color
        output[bottom][col] = frame_color
    for row in range(top, bottom + 1):
        output[row][left] = frame_color
        output[row][right] = frame_color

    inner_height = bottom - top - 1
    inner_width = right - left - 1
    horizontal_length = sum(piece["width"] for piece in pieces) + len(pieces) - 1
    vertical_length = sum(piece["height"] for piece in pieces) + len(pieces) - 1
    horizontal_fits = (
        horizontal_length <= inner_width
        and max(piece["height"] for piece in pieces) <= inner_height
    )
    vertical_fits = (
        vertical_length <= inner_height
        and max(piece["width"] for piece in pieces) <= inner_width
    )
    horizontal = horizontal_fits and (not vertical_fits or inner_width >= inner_height)

    if horizontal:
        pieces = [record[2] for record in sorted(((piece["center_col"],piece["center_row"]),index,piece) for index,piece in enumerate(pieces))]
        col = left + 1 + (inner_width - horizontal_length) // 2
        for piece in pieces:
            row = top + 1 + (inner_height - piece["height"]) // 2
            for r in range(row, row + piece["height"]):
                for c in range(col, col + piece["width"]):
                    output[r][c] = piece["color"]
            col += piece["width"] + 1
    else:
        pieces = [record[2] for record in sorted(((piece["center_row"],piece["center_col"]),index,piece) for index,piece in enumerate(pieces))]
        row = top + 1 + (inner_height - vertical_length) // 2
        for piece in pieces:
            col = left + 1 + (inner_width - piece["width"]) // 2
            for r in range(row, row + piece["height"]):
                for c in range(col, col + piece["width"]):
                    output[r][c] = piece["color"]
            row += piece["height"] + 1

    return output
