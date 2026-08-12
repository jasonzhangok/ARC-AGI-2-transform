def transform(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]

    template = None
    for top in range(height - 2):
        for left in range(width - 2):
            block = [
                grid[top + row][left + col]
                for row in range(3)
                for col in range(3)
            ]
            if all(value in (4, 6) for value in block) and 4 in block and 6 in block:
                template = tuple(
                    tuple(grid[top + row][left + col] == 6 for col in range(3))
                    for row in range(3)
                )
                break
        if template is not None:
            break

    variants = []
    current = template
    for _ in range(4):
        reflected = tuple(tuple(reversed(row)) for row in current)
        for candidate in (current, reflected):
            if candidate not in variants:
                variants.append(candidate)
        current = tuple(
            tuple(current[2 - col][row] for col in range(3))
            for row in range(3)
        )

    for pattern in variants:
        anchors = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if pattern[row][col]
        ]
        targets = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if not pattern[row][col]
        ]

        for top in range(-2, height):
            for left in range(-2, width):
                if not all(
                    0 <= top + row < height
                    and 0 <= left + col < width
                    and grid[top + row][left + col] == 6
                    for row, col in anchors
                ):
                    continue

                visible_targets = [
                    (top + row, left + col)
                    for row, col in targets
                    if 0 <= top + row < height and 0 <= left + col < width
                ]
                if not visible_targets or any(
                    grid[row][col] == 6 for row, col in visible_targets
                ):
                    continue

                for row, col in visible_targets:
                    output[row][col] = 4

    return output
