def transform(grid):
    height = len(grid)
    width = len(grid[0])
    frames = []

    for color in range(1, 10):
        cells = [
            (row, column)
            for row in range(height)
            for column in range(width)
            if grid[row][column] == color
        ]
        if not cells:
            continue
        top = min(row for row, column in cells)
        bottom = max(row for row, column in cells)
        left = min(column for row, column in cells)
        right = max(column for row, column in cells)
        if (
            bottom - top >= 2
            and right - left >= 2
            and all(
                grid[top][column] == color and grid[bottom][column] == color
                for column in range(left, right + 1)
            )
            and all(
                grid[row][left] == color and grid[row][right] == color
                for row in range(top, bottom + 1)
            )
        ):
            frames.append((color, top, bottom, left, right))

    donor = next(
        frame
        for frame in frames
        if any(
            grid[row][column] == frame[0]
            for row in range(frame[1] + 1, frame[2])
            for column in range(frame[3] + 1, frame[4])
        )
    )
    donor_color, donor_top, donor_bottom, donor_left, donor_right = donor
    frame_height = donor_bottom - donor_top + 1
    frame_width = donor_right - donor_left + 1
    pattern = [
        [
            grid[donor_top + row + 1][donor_left + column + 1] == donor_color
            for column in range(frame_width - 2)
        ]
        for row in range(frame_height - 2)
    ]

    output = [[0 for _ in range(width)] for _ in range(height)]
    for color, top, bottom, left, right in frames:
        if bottom - top + 1 != frame_height or right - left + 1 != frame_width:
            continue
        for row in range(top, bottom + 1):
            for column in range(left, right + 1):
                if (
                    row in (top, bottom)
                    or column in (left, right)
                    or pattern[row - top - 1][column - left - 1]
                ):
                    output[row][column] = color

    return output
