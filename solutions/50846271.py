def transform(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    result = [row[:] for row in grid]
    marked = frozenset(
        (row, col)
        for row in range(height)
        for col in range(width)
        if grid[row][col] == 2
    )

    solved = not marked
    for radius in range(1, max(height, width)) if marked else ():
        candidates = []
        for row in range(height):
            for col in range(width):
                cells = {(row, other) for other in range(max(0, col - radius),
                                                          min(width, col + radius + 1))}
                cells.update((other, col) for other in range(max(0, row - radius),
                                                             min(height, row + radius + 1)))
                cells = frozenset(cells)
                covered = cells & marked
                if (len(covered) >= 3
                        and all(grid[r][c] in (2, 5) for r, c in cells)):
                    candidates.append((cells, covered))

        containing = {position: [] for position in marked}
        for index, (_, covered) in enumerate(candidates):
            for position in covered:
                containing[position].append(index)

        stack = [(frozenset(), ())]
        selected = None
        while stack and selected is None:
            covered, chosen = stack.pop()
            if covered == marked:
                selected = chosen
                break
            uncovered = marked - covered
            position = None
            position_score = None
            for point in uncovered:
                score = sum(not (candidates[index][1] & covered) for index in containing[point])
                if position is None or score < position_score:
                    position = point
                    position_score = score
            options = [index for index in containing[position] if not candidates[index][1] & covered]
            for index in reversed(options):
                stack.append((covered | candidates[index][1], chosen + (index,)))
        if selected is not None:
            for index in selected:
                for row, col in candidates[index][0]:
                    if grid[row][col] == 5:
                        result[row][col] = 8
            solved = True
            break
    output = result
    return output
