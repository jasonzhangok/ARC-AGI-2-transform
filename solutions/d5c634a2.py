def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    all_cells = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 2:
                all_cells.append((row, col))

    candidates = []

    for row in range(height - 1):
        for col in range(width - 2):
            if (
                grid[row][col] == 2
                and grid[row][col + 1] == 2
                and grid[row][col + 2] == 2
                and grid[row + 1][col + 1] == 2
            ):
                candidates.append((
                    ((row, col), (row, col + 1), (row, col + 2),
                     (row + 1, col + 1)),
                    1,
                ))
            if (
                grid[row][col + 1] == 2
                and grid[row + 1][col] == 2
                and grid[row + 1][col + 1] == 2
                and grid[row + 1][col + 2] == 2
            ):
                candidates.append((
                    ((row, col + 1), (row + 1, col),
                     (row + 1, col + 1), (row + 1, col + 2)),
                    -1,
                ))

    candidates_by_cell = {}
    for index in range(len(candidates)):
        for cell in candidates[index][0]:
            if cell not in candidates_by_cell:
                candidates_by_cell[cell] = []
            candidates_by_cell[cell].append(index)

    chosen = []
    stack = [(set(), [])]
    while stack:
        used, selection = stack.pop()
        if len(used) == len(all_cells):
            chosen = selection
            break
        target = None
        for cell in all_cells:
            if cell not in used:
                target = cell
                break
        if target not in candidates_by_cell:
            continue
        for index in candidates_by_cell[target]:
            cells = candidates[index][0]
            overlaps = False
            for cell in cells:
                if cell in used:
                    overlaps = True
                    break
            if not overlaps:
                next_used = set(used)
                for cell in cells:
                    next_used.add(cell)
                stack.append((next_used, selection + [index]))

    upward = 0
    downward = 0
    for index in chosen:
        if candidates[index][1] == 1:
            upward += 1
        else:
            downward += 1

    output = [[0 for _ in range(6)] for _ in range(3)]
    positions = ((0, 0), (2, 0), (0, 2), (2, 2))
    for index in range(min(downward, 4)):
        row, col = positions[index]
        output[row][col] = 3
    for index in range(min(upward, 4)):
        row, col = positions[index]
        output[row][col + 3] = 1
    return output
