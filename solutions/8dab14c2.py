def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for source_row in grid:
        for value in source_row:
            counts[value] = counts.get(value, 0) + 1
    background = None
    for value in counts:
        if background is None or counts[value] > counts[background]:
            background = value
    output = [row[:] for row in grid]

    for color in {value for row in grid for value in row if value != background}:
        candidates = []
        for top in range(height - 2):
            for bottom in range(top + 2, height):
                for left in range(width - 2):
                    for right in range(left + 2, width):
                        rectangle_height = bottom - top + 1
                        rectangle_width = right - left + 1
                        if rectangle_height == rectangle_width:
                            continue
                        if not all(grid[row][col] == color
                                   for row in range(top + 1, bottom)
                                   for col in range(left + 1, right)):
                            continue
                        boundary = ([(top, col) for col in range(left, right + 1)]
                                    + [(bottom, col) for col in range(left, right + 1)]
                                    + [(row, left) for row in range(top + 1, bottom)]
                                    + [(row, right) for row in range(top + 1, bottom)])
                        gaps = [point for point in boundary
                                if grid[point[0]][point[1]] != color]
                        if any(grid[row][col] != background for row, col in gaps):
                            continue
                        if any(abs(row - other_row) + abs(col - other_col) == 1
                               for index, (row, col) in enumerate(gaps)
                               for other_row, other_col in gaps[index + 1:]):
                            continue
                        valid = True
                        sides = (
                            ([(top, col) for col in range(left, right + 1)], -1, 0),
                            ([(bottom, col) for col in range(left, right + 1)], 1, 0),
                            ([(row, left) for row in range(top, bottom + 1)], 0, -1),
                            ([(row, right) for row in range(top, bottom + 1)], 0, 1),
                        )
                        for side, d_row, d_col in sides:
                            exposed = [(row, col) for row, col in side
                                       if grid[row][col] == background
                                       and 0 <= row + d_row < height
                                       and 0 <= col + d_col < width
                                       and grid[row + d_row][col + d_col] == background]
                            if len(exposed) > 1:
                                valid = False
                                break
                        if not valid:
                            continue
                        all_gaps_exposed = True
                        for row, col in gaps:
                            directions = []
                            if row == top: directions.append((-1, 0))
                            if row == bottom: directions.append((1, 0))
                            if col == left: directions.append((0, -1))
                            if col == right: directions.append((0, 1))
                            if not any(0 <= row + d_row < height
                                       and 0 <= col + d_col < width
                                       and grid[row + d_row][col + d_col] == background
                                       for d_row, d_col in directions):
                                all_gaps_exposed = False
                                break
                        if all_gaps_exposed:
                            candidates.append((top, bottom, left, right))

        rectangles = []
        for horizontal in (True, False):
            oriented = [rectangle for rectangle in candidates
                        if ((rectangle[3] - rectangle[2]
                             > rectangle[1] - rectangle[0]) == horizontal)]
            if oriented:
                scored = [((rectangle[1] - rectangle[0] + 1)
                           * (rectangle[3] - rectangle[2] + 1),
                           -index, rectangle)
                          for index, rectangle in enumerate(oriented)]
                rectangles.append(max(scored)[2])

        events = {}
        for rectangle in rectangles:
            top, bottom, left, right = rectangle
            perimeter = ([(top, col) for col in range(left, right + 1)]
                         + [(bottom, col) for col in range(left, right + 1)]
                         + [(row, left) for row in range(top + 1, bottom)]
                         + [(row, right) for row in range(top + 1, bottom)])
            for row, col in perimeter:
                directions = []
                if row == top: directions.append((-1, 0))
                if row == bottom: directions.append((1, 0))
                if col == left: directions.append((0, -1))
                if col == right: directions.append((0, 1))
                for d_row, d_col in directions:
                    opposite = (row - d_row * (bottom - top),
                                col - d_col * (right - left))
                    outside = row + d_row, col + d_col
                    if (grid[row][col] == background
                            and 0 <= outside[0] < height
                            and 0 <= outside[1] < width
                            and grid[outside[0]][outside[1]] == background):
                        target = opposite[0] - d_row, opposite[1] - d_col
                        if 0 <= target[0] < height and 0 <= target[1] < width:
                            events.setdefault(("gap", (row, col)), set()).add(
                                (rectangle, opposite, target, color))
                    elif (0 <= outside[0] < height
                          and 0 <= outside[1] < width
                          and grid[outside[0]][outside[1]] == color):
                        beyond_row = outside[0] + d_row
                        beyond_col = outside[1] + d_col
                        isolated = not (0 <= beyond_row < height
                                        and 0 <= beyond_col < width
                                        and grid[beyond_row][beyond_col] != background)
                        tangent = d_col, -d_row
                        for sign in (-1, 1):
                            next_row = outside[0] + sign * tangent[0]
                            next_col = outside[1] + sign * tangent[1]
                            if (0 <= next_row < height and 0 <= next_col < width
                                    and grid[next_row][next_col] == color):
                                isolated = False
                        if isolated:
                            events.setdefault(("bump", outside), set()).add(
                                (rectangle, opposite, opposite, background))

        for hypotheses in events.values():
            owners = hypotheses
            if len({hypothesis[0] for hypothesis in hypotheses}) > 1:
                cover_counts = {}
                for hypothesis in hypotheses:
                    point = hypothesis[1]
                    cover_counts[hypothesis] = sum(
                        other != hypothesis[0]
                        and other[0] <= point[0] <= other[1]
                        and other[2] <= point[1] <= other[3]
                        for other in rectangles)
                least_covered = min(cover_counts.values())
                owners = {hypothesis for hypothesis in hypotheses
                          if cover_counts[hypothesis] == least_covered}
            for _, _, target, value in owners:
                output[target[0]][target[1]] = value
    return output
