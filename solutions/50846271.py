"""Complete the partially marked, equally sized plus signs."""


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

    if not marked:
        return result

    def cross(row, col, radius):
        cells = {(row, other) for other in range(max(0, col - radius),
                                                  min(width, col + radius + 1))}
        cells.update((other, col) for other in range(max(0, row - radius),
                                                     min(height, row + radius + 1)))
        return frozenset(cells)

    for radius in range(1, max(height, width)):
        candidates = []
        for row in range(height):
            for col in range(width):
                cells = cross(row, col, radius)
                covered = cells & marked
                if (len(covered) >= 3
                        and all(grid[r][c] in (2, 5) for r, c in cells)):
                    candidates.append((cells, covered))

        containing = {position: [] for position in marked}
        for index, (_, covered) in enumerate(candidates):
            for position in covered:
                containing[position].append(index)

        failed = set()

        def exact_cover(covered):
            if covered == marked:
                return ()
            if covered in failed:
                return None

            position = min(
                marked - covered,
                key=lambda point: sum(
                    not (candidates[index][1] & covered)
                    for index in containing[point]
                ),
            )
            for index in containing[position]:
                candidate_marked = candidates[index][1]
                if candidate_marked & covered:
                    continue
                remainder = exact_cover(covered | candidate_marked)
                if remainder is not None:
                    return (index,) + remainder

            failed.add(covered)
            return None

        selected = exact_cover(frozenset())
        if selected is not None:
            for index in selected:
                for row, col in candidates[index][0]:
                    if grid[row][col] == 5:
                        result[row][col] = 8
            return result

    return result
