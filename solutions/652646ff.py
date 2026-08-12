def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)

    ring = ((0, 2), (0, 3), (1, 1), (1, 4),
            (2, 0), (2, 5), (3, 0), (3, 5),
            (4, 1), (4, 4), (5, 2), (5, 3))
    colors = []
    positions = {}
    for color in counts:
        if color == background:
            continue
        best_score = None
        best_position = None
        for top in range(-5, height):
            for left in range(-5, width):
                matches = 0
                occupied = 0
                visible = 0
                for dr, dc in ring:
                    row = top + dr
                    col = left + dc
                    if 0 <= row < height and 0 <= col < width:
                        visible += 1
                        value = grid[row][col]
                        if value == color:
                            matches += 1
                        if value != background:
                            occupied += 1
                score = (matches, occupied - visible, occupied, visible)
                if best_score is None or score > best_score:
                    best_score = score
                    best_position = (top, left)
        if best_score[0] >= 8 and best_score[1] == 0:
            colors.append(color)
            positions[color] = best_position

    above = set()
    for first_index in range(len(colors)):
        first = colors[first_index]
        first_top, first_left = positions[first]
        first_cells = set()
        for dr, dc in ring:
            row = first_top + dr
            col = first_left + dc
            if 0 <= row < height and 0 <= col < width:
                first_cells.add((row, col))
        for second_index in range(first_index + 1, len(colors)):
            second = colors[second_index]
            second_top, second_left = positions[second]
            first_wins = 0
            second_wins = 0
            for dr, dc in ring:
                row = second_top + dr
                col = second_left + dc
                if (row, col) in first_cells:
                    value = grid[row][col]
                    if value == first:
                        first_wins += 1
                    elif value == second:
                        second_wins += 1
            if first_wins > second_wins:
                above.add((first, second))
            elif second_wins > first_wins:
                above.add((second, first))

    ordered = []
    remaining = colors[:]
    while remaining:
        next_color = None
        for color in remaining:
            has_predecessor = False
            for other in remaining:
                if (other, color) in above:
                    has_predecessor = True
                    break
            if not has_predecessor:
                next_color = color
                break
        if next_color is None:
            next_color = remaining[0]
        ordered.append(next_color)
        remaining.remove(next_color)

    output = []
    for color in ordered:
        for row_index in range(6):
            row = [background] * 6
            for dr, dc in ring:
                if dr == row_index:
                    row[dc] = color
            output.append(row)
    return output
