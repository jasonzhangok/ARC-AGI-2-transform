from collections import Counter


def _sampled_frame(points):
    """Return the bounding box when points are a two-spaced rectangle frame."""
    top = min(row for row, _ in points)
    bottom = max(row for row, _ in points)
    left = min(col for _, col in points)
    right = max(col for _, col in points)
    if top == bottom or left == right:
        return None

    rows = range(top, bottom + 1, 2)
    cols = range(left, right + 1, 2)
    expected = (
        {(top, col) for col in cols}
        | {(bottom, col) for col in cols}
        | {(row, left) for row in rows}
        | {(row, right) for row in rows}
    )
    if points == expected:
        return top, left, bottom, right
    return None


def _sampled_components(grid, ignored):
    """Find colored objects whose pixels are adjacent at the grid's two-cell pitch."""
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] not in ignored
    }
    components = []
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        stack = [start]
        points = {start}
        while stack:
            row, col = stack.pop()
            for dr, dc in ((-2, 0), (2, 0), (0, -2), (0, 2)):
                point = row + dr, col + dc
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    points.add(point)
                    stack.append(point)
        components.append((color, points))
    return components


def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background, lattice = (color for color, _ in counts.most_common(2))

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
    frames = [
        (box, color)
        for color, points in positions.items()
        if (box := _sampled_frame(points)) is not None
    ]
    (top, left, bottom, right), frame_color = max(
        frames,
        key=lambda item: (item[0][2] - item[0][0]) * (item[0][3] - item[0][1]),
    )

    pieces = []
    for color, points in _sampled_components(
        grid, {background, lattice, frame_color}
    ):
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
        pieces.sort(key=lambda piece: (piece["center_col"], piece["center_row"]))
        col = left + 1 + (inner_width - horizontal_length) // 2
        for piece in pieces:
            row = top + 1 + (inner_height - piece["height"]) // 2
            for r in range(row, row + piece["height"]):
                for c in range(col, col + piece["width"]):
                    output[r][c] = piece["color"]
            col += piece["width"] + 1
    else:
        pieces.sort(key=lambda piece: (piece["center_row"], piece["center_col"]))
        row = top + 1 + (inner_height - vertical_length) // 2
        for piece in pieces:
            col = left + 1 + (inner_width - piece["width"]) // 2
            for r in range(row, row + piece["height"]):
                for c in range(col, col + piece["width"]):
                    output[r][c] = piece["color"]
            row += piece["height"] + 1

    return output
