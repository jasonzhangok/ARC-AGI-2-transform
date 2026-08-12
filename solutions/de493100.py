def transform(grid):
    height = len(grid)
    width = len(grid[0])
    marker = 7

    best_row_score = -1
    best_row_pairs = -1
    row_reflection = None
    for reflection in range(1, 2 * height - 2):
        matches = 0
        pairs = 0
        for row in range(height):
            reflected_row = reflection - row
            if 0 <= reflected_row < height:
                for column in range(width):
                    if (grid[row][column] != marker
                            and grid[reflected_row][column] != marker):
                        pairs += 1
                        if grid[row][column] == grid[reflected_row][column]:
                            matches += 1
        if pairs >= height * width // 4:
            score = matches / pairs
            if (score > best_row_score
                    or score == best_row_score and pairs > best_row_pairs):
                best_row_score = score
                best_row_pairs = pairs
                row_reflection = reflection

    best_column_score = -1
    best_column_pairs = -1
    column_reflection = None
    for reflection in range(1, 2 * width - 2):
        matches = 0
        pairs = 0
        for column in range(width):
            reflected_column = reflection - column
            if 0 <= reflected_column < width:
                for row in range(height):
                    if (grid[row][column] != marker
                            and grid[row][reflected_column] != marker):
                        pairs += 1
                        if grid[row][column] == grid[row][reflected_column]:
                            matches += 1
        if pairs >= height * width // 4:
            score = matches / pairs
            if (score > best_column_score
                    or score == best_column_score and pairs > best_column_pairs):
                best_column_score = score
                best_column_pairs = pairs
                column_reflection = reflection

    marker_cells = []
    for row in range(height):
        for column in range(width):
            if grid[row][column] == marker:
                marker_cells.append((row, column))
    top = min(cell[0] for cell in marker_cells)
    bottom = max(cell[0] for cell in marker_cells)
    left = min(cell[1] for cell in marker_cells)
    right = max(cell[1] for cell in marker_cells)
    output_height = bottom - top + 1
    output_width = right - left + 1
    output = [[None for _ in range(output_width)] for _ in range(output_height)]

    for output_row in range(output_height):
        for output_column in range(output_width):
            row = top + output_row
            column = left + output_column
            orbit = ((row_reflection - row, column),
                     (row, column_reflection - column),
                     (row_reflection - row, column_reflection - column))
            for source_row, source_column in orbit:
                if (0 <= source_row < height and 0 <= source_column < width
                        and grid[source_row][source_column] != marker):
                    output[output_row][output_column] = grid[source_row][source_column]
                    break

    for output_column in range(output_width):
        output_row = 0
        while output_row < output_height:
            if output[output_row][output_column] is not None:
                output_row += 1
                continue
            run_start = output_row
            while (output_row < output_height
                   and output[output_row][output_column] is None):
                output_row += 1
            run_end = output_row - 1

            template_column = None
            template_distance = output_width + 1
            for candidate_column in range(output_width):
                complete = True
                for row in range(run_start, run_end + 1):
                    if output[row][candidate_column] is None:
                        complete = False
                        break
                distance = abs(candidate_column - output_column)
                if complete and distance < template_distance:
                    template_distance = distance
                    template_column = candidate_column

            if template_column is None:
                continue
            if run_start > 0:
                upper_color = output[run_start - 1][output_column]
            elif top > 0 and grid[top - 1][left + output_column] != marker:
                upper_color = grid[top - 1][left + output_column]
            else:
                upper_color = None
            if run_end + 1 < output_height:
                lower_color = output[run_end + 1][output_column]
            elif bottom + 1 < height and grid[bottom + 1][left + output_column] != marker:
                lower_color = grid[bottom + 1][left + output_column]
            else:
                lower_color = upper_color

            template_edge = output[run_start][template_column]
            for row in range(run_start, run_end + 1):
                template_value = output[row][template_column]
                if template_value != template_edge:
                    output[row][output_column] = template_value
                elif row - run_start <= run_end - row and upper_color is not None:
                    output[row][output_column] = upper_color
                elif lower_color is not None:
                    output[row][output_column] = lower_color
                else:
                    output[row][output_column] = template_value
    return output
