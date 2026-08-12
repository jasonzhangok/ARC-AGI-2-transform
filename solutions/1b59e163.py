def transform(grid):
    height = len(grid)
    width = len(grid[0])

    color_counts = {}
    color_positions = {}
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            color_counts[color] = color_counts.get(color, 0) + 1
            if color not in color_positions:
                color_positions[color] = []
            color_positions[color].append((row, col))
    background = 0
    background_count = -1
    for color in color_counts:
        if color_counts[color] > background_count:
            background = color
            background_count = color_counts[color]

    output = [[background for col in range(width)] for row in range(height)]
    for anchor_color in color_positions:
        anchors = color_positions[anchor_color]
        if anchor_color == background or len(anchors) < 2:
            continue

        attached_anchors = []
        for anchor_row, anchor_col in anchors:
            attached = False
            for row_offset in (-1, 0, 1):
                for col_offset in (-1, 0, 1):
                    if row_offset == 0 and col_offset == 0:
                        continue
                    row = anchor_row + row_offset
                    col = anchor_col + col_offset
                    if 0 <= row < height and 0 <= col < width:
                        if grid[row][col] not in (background, anchor_color):
                            attached = True
            if attached:
                attached_anchors.append((anchor_row, anchor_col))
        if len(attached_anchors) != 1:
            continue

        template_row, template_col = attached_anchors[0]
        neighbor_color_counts = {}
        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):
                if row_offset == 0 and col_offset == 0:
                    continue
                row = template_row + row_offset
                col = template_col + col_offset
                if 0 <= row < height and 0 <= col < width:
                    color = grid[row][col]
                    if color not in (background, anchor_color):
                        neighbor_color_counts[color] = neighbor_color_counts.get(color, 0) + 1
        pattern_color = background
        pattern_neighbor_count = -1
        for color in neighbor_color_counts:
            if neighbor_color_counts[color] > pattern_neighbor_count:
                pattern_color = color
                pattern_neighbor_count = neighbor_color_counts[color]

        stack = []
        pattern_cells = set()
        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):
                row = template_row + row_offset
                col = template_col + col_offset
                if 0 <= row < height and 0 <= col < width:
                    if grid[row][col] == pattern_color:
                        pattern_cells.add((row, col))
                        stack.append((row, col))
        while stack:
            row, col = stack.pop()
            for row_offset in (-1, 0, 1):
                for col_offset in (-1, 0, 1):
                    if row_offset == 0 and col_offset == 0:
                        continue
                    next_row = row + row_offset
                    next_col = col + col_offset
                    next_cell = (next_row, next_col)
                    if 0 <= next_row < height and 0 <= next_col < width:
                        if grid[next_row][next_col] == pattern_color:
                            if next_cell not in pattern_cells:
                                pattern_cells.add(next_cell)
                                stack.append(next_cell)

        offsets = []
        for row, col in pattern_cells:
            offsets.append((row - template_row, col - template_col))
        for anchor_row, anchor_col in anchors:
            if (anchor_row, anchor_col) == (template_row, template_col):
                continue
            output[anchor_row][anchor_col] = anchor_color
            for row_offset, col_offset in offsets:
                row = anchor_row + row_offset
                col = anchor_col + col_offset
                if 0 <= row < height and 0 <= col < width:
                    output[row][col] = pattern_color

    return output
