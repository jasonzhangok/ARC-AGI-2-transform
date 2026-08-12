def transform(grid):
    height = len(grid)
    width = len(grid[0])
    result = [row[:] for row in grid]
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    best = None
    for orientation in range(2):
        line_count = height if orientation == 0 else width
        line_length = width if orientation == 0 else height
        candidates = []
        for line_index in range(line_count):
            color = None
            positions = []
            clean = True
            for offset in range(line_length):
                value = grid[line_index][offset] if orientation == 0 else grid[offset][line_index]
                if value != background:
                    if color is None:
                        color = value
                    elif value != color:
                        clean = False
                        break
                    positions.append(offset)
            if clean and color is not None:
                candidates.append((line_index, color, positions))
        for first in candidates:
            for second in candidates:
                if first[0] == second[0] or first[1] == second[1] or first[2] != second[2]:
                    continue
                score = 0
                for axis in range(line_count):
                    outside = first[0] < second[0] and axis < first[0] or (first[0] > second[0] and axis > first[0])
                    if not outside:
                        continue
                    target_axis = second[0] + first[0] - axis
                    if target_axis < 0 or target_axis >= line_count:
                        continue
                    for offset in range(line_length):
                        value = grid[axis][offset] if orientation == 0 else grid[offset][axis]
                        if value == second[1]:
                            score += 1
                if best is None or score > best[0]:
                    best = (score, orientation, first[0], second[0], first[1], second[1])
    if best is None or best[0] == 0:
        output = result
    else:
        _, orientation, first_line, second_line, paint, source = best
        line_count = height if orientation == 0 else width
        line_length = width if orientation == 0 else height
        for axis in range(line_count):
            outside = first_line < second_line and axis < first_line or (first_line > second_line and axis > first_line)
            if not outside:
                continue
            target_axis = second_line + first_line - axis
            if target_axis < 0 or target_axis >= line_count:
                continue
            for offset in range(line_length):
                value = grid[axis][offset] if orientation == 0 else grid[offset][axis]
                if value == source:
                    if orientation == 0:
                        result[target_axis][offset] = paint
                    else:
                        result[offset][target_axis] = paint
        output = result
    return output
