def transform(grid):
    height, width = len(grid), len(grid[0])
    zero_rows = [
        row for row in range(height)
        if all(value == 0 for value in grid[row])
    ]
    zero_cols = [
        col for col in range(width)
        if all(grid[row][col] == 0 for row in range(height))
    ]

    marker = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 6
    ]
    marker_top = min(row for row, _ in marker)
    marker_bottom = max(row for row, _ in marker)
    marker_left = min(col for _, col in marker)
    marker_right = max(col for _, col in marker)

    output = [row[:] for row in grid]
    horizontal_separators = [row for row in zero_rows if 0 < row < height - 1]
    vertical_separators = [col for col in zero_cols if 0 < col < width - 1]

    if len(vertical_separators) > len(horizontal_separators):
        _length = width
        _separators = zero_cols
        separator_set = set(_separators)
        bands = []
        start = 0
        for position in range(_length + 1):
            if position == _length or position in separator_set:
                if start < position:
                    bands.append(range(start, position))
                start = position + 1
        _bands_result_1 = bands
        bands = _bands_result_1
        band_of = {col: index for index, band in enumerate(bands) for col in band}
        marker_band = band_of[marker_left]
        step = marker_bottom - marker_top + 1
        for row in range(height):
            longitudinal_distance = max(marker_top - row, row - marker_bottom, 0)
            radius = (longitudinal_distance + step - 1) // step
            for col in range(width):
                if (grid[row][col] == 8 and col in band_of
                        and 0 < abs(band_of[col] - marker_band) <= radius):
                    output[row][col] = 4
    else:
        _length = height
        _separators = zero_rows
        separator_set = set(_separators)
        bands = []
        start = 0
        for position in range(_length + 1):
            if position == _length or position in separator_set:
                if start < position:
                    bands.append(range(start, position))
                start = position + 1
        _bands_result_2 = bands
        bands = _bands_result_2
        band_of = {row: index for index, band in enumerate(bands) for row in band}
        marker_band = band_of[marker_top]
        step = marker_right - marker_left + 1
        for row in range(height):
            if row not in band_of:
                continue
            band_distance = abs(band_of[row] - marker_band)
            for col in range(width):
                longitudinal_distance = max(marker_left - col, col - marker_right, 0)
                radius = (longitudinal_distance + step - 1) // step
                if grid[row][col] == 8 and 0 < band_distance <= radius:
                    output[row][col] = 4

    return output
