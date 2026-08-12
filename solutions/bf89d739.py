def transform(grid):
    output = [row[:] for row in grid]
    markers = [
        (row, col)
        for row, values in enumerate(grid)
        for col, value in enumerate(values)
        if value == 2
    ]

    first, second = next(
        (first, second)
        for index, first in enumerate(markers)
        for second in markers[index + 1 :]
        if first[0] == second[0] or first[1] == second[1]
    )

    if first[0] == second[0]:
        backbone_row = first[0]
        left, right = sorted((first[1], second[1]))
        for col in range(left, right + 1):
            if output[backbone_row][col] == 0:
                output[backbone_row][col] = 3
        for row, col in markers:
            if (row, col) not in (first, second):
                top, bottom = sorted((row, backbone_row))
                for branch_row in range(top, bottom + 1):
                    if output[branch_row][col] == 0:
                        output[branch_row][col] = 3
    else:
        backbone_col = first[1]
        top, bottom = sorted((first[0], second[0]))
        for row in range(top, bottom + 1):
            if output[row][backbone_col] == 0:
                output[row][backbone_col] = 3
        for row, col in markers:
            if (row, col) not in (first, second):
                left, right = sorted((col, backbone_col))
                for branch_col in range(left, right + 1):
                    if output[row][branch_col] == 0:
                        output[row][branch_col] = 3

    return output
