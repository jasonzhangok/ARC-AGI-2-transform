def transform(grid):
    stencil = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value == 1
    ]
    top, bottom = min(r for r, _ in stencil), max(r for r, _ in stencil)
    left, right = min(c for _, c in stencil), max(c for _, c in stencil)
    shape = {(r - top, c - left) for r, c in stencil}
    height, width = bottom - top + 1, right - left + 1
    markers = sorted(
        (r, c, value)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value not in (0, 1)
    )

    horizontal = len({r for r, _, _ in markers}) == 1
    out_height = height if horizontal else height * len(markers)
    out_width = width * len(markers) if horizontal else width
    output = [[0] * out_width for _ in range(out_height)]
    for index, (_, _, color) in enumerate(markers):
        row_offset = 0 if horizontal else index * height
        column_offset = index * width if horizontal else 0
        for r, c in shape:
            output[row_offset + r][column_offset + c] = color
    return output
