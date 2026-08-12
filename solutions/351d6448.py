def transform(grid):
    separators = []
    for row in range(len(grid)):
        if all(value == 5 for value in grid[row]):
            separators.append(row)
    cuts = [-1] + separators + [len(grid)]
    panels = []
    for index in range(len(cuts) - 1):
        panels.append(grid[cuts[index] + 1:cuts[index + 1]])
    height = len(panels[0])
    width = len(grid[0])
    output = [[0 for col in range(width)] for row in range(height)]

    colors = set()
    for panel in panels:
        for row in panel:
            for color in row:
                if color != 0:
                    colors.add(color)
    for color in sorted(colors):
        for row in range(height):
            intervals = []
            for panel in panels:
                positions = []
                for col in range(width):
                    if panel[row][col] == color:
                        positions.append(col)
                if positions:
                    runs = []
                    for col in positions:
                        if not runs or col > runs[-1][1] + 1:
                            runs.append([col, col])
                        else:
                            runs[-1][1] = col
                    intervals.append(runs)
            if len(intervals) < 2:
                continue
            previous_runs = intervals[-2]
            current_runs = intervals[-1]
            if len(previous_runs) != len(current_runs):
                continue
            for run_index in range(len(current_runs)):
                next_left = 2 * current_runs[run_index][0] - previous_runs[run_index][0]
                next_right = 2 * current_runs[run_index][1] - previous_runs[run_index][1]
                for col in range(next_left, next_right + 1):
                    if 0 <= col < width:
                        output[row][col] = color

    spreading_colors = []
    if len(panels) >= 2:
        for color in colors:
            previous_count = 0
            current_count = 0
            for row in range(height):
                for col in range(width):
                    if panels[-2][row][col] == color:
                        previous_count += 1
                    if panels[-1][row][col] == color:
                        current_count += 1
            if current_count > previous_count:
                spreading_colors.append(color)
    for color in spreading_colors:
        for row in range(height):
            for col in range(width):
                if panels[-1][row][col] in (0, color):
                    continue
                touches = False
                for row_offset in (-1, 0, 1):
                    for col_offset in (-1, 0, 1):
                        next_row = row + row_offset
                        next_col = col + col_offset
                        if 0 <= next_row < height and 0 <= next_col < width:
                            if panels[-1][next_row][next_col] == color:
                                touches = True
                if touches:
                    output[row][col] = color

    return output
