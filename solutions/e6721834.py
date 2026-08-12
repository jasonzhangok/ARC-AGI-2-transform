def transform(grid):
    height, width = len(grid), len(grid[0])
    choices = []
    if width % 2 == 0:
        choices.append(
            (
                [row[: width // 2] for row in grid],
                [row[width // 2 :] for row in grid],
            )
        )
    if height % 2 == 0:
        choices.append((grid[: height // 2], grid[height // 2 :]))
    best_pair = None
    best_score = None
    for pair in choices:
        score = 0
        for half in pair:
            counts = {}
            for value in (value for row in half for value in row):
                counts[value] = counts.get(value, 0) + 1
            score += max(counts.values())
        if best_pair is None or score > best_score:
            best_pair = pair
            best_score = score
    first, second = best_pair
    counts = {}
    for value in (value for row in first for value in row):
        counts[value] = counts.get(value, 0) + 1
    first_bg = max(counts, key=counts.get)
    first_fg = sum(value != first_bg for row in first for value in row)
    counts = {}
    for value in (value for row in second for value in row):
        counts[value] = counts.get(value, 0) + 1
    second_bg = max(counts, key=counts.get)
    second_fg = sum(value != second_bg for row in second for value in row)
    if first_fg > second_fg:
        templates, targets = first, second
        template_background = first_bg
        target_background = second_bg
    else:
        templates, targets = second, first
        template_background = second_bg
        target_background = first_bg
    height, width = len(targets), len(targets[0])
    body_counts = {}
    for value in (
        value for row in templates for value in row if value != template_background
    ):
        body_counts[value] = body_counts.get(value, 0) + 1
    body_color = max(body_counts, key=body_counts.get)
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if templates[row][col] == template_background or (row, col) in seen:
                continue
            component = []
            stack = [(row, col)]
            seen.add((row, col))
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_step
                    next_col = current_col + col_step
                    next_cell = (next_row, next_col)
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and next_cell not in seen
                        and templates[next_row][next_col] != template_background
                    ):
                        seen.add(next_cell)
                        stack.append(next_cell)
            components.append(component)
    output = [[target_background] * width for _ in range(height)]
    for component in components:
        anchors = [
            (row, col, templates[row][col])
            for row, col in component
            if templates[row][col] != body_color
        ]
        anchor_row, anchor_col, anchor_color = anchors[0]
        translations = []
        for target_row in range(height):
            for target_col in range(width):
                if targets[target_row][target_col] != anchor_color:
                    continue
                row_offset = target_row - anchor_row
                col_offset = target_col - anchor_col
                if all(
                    0 <= row + row_offset < height
                    and 0 <= col + col_offset < width
                    and targets[row + row_offset][col + col_offset] == color
                    for row, col, color in anchors
                ):
                    translations.append((row_offset, col_offset))
        if len(translations) != 1:
            continue
        row_offset, col_offset = translations[0]
        for row, col in component:
            output[row + row_offset][col + col_offset] = templates[row][col]
    return output
