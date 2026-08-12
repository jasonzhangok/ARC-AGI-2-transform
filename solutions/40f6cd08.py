def transform(grid):
    if not grid:
        output = []
    else:
        height, width = len(grid), len(grid[0])
        counts = {}
        for source_row in grid:
            for value in source_row:
                counts[value] = counts.get(value, 0) + 1
        background = None
        for value in counts:
            if background is None or counts[value] > counts[background]:
                background = value

        unseen = {(row, col) for row in range(height) for col in range(width)
                  if grid[row][col] != background}
        components = []
        while unseen:
            start = unseen.pop()
            component = [start]
            stack = [start]
            while stack:
                row, col = stack.pop()
                for neighbor in ((row - 1, col), (row + 1, col),
                                 (row, col - 1), (row, col + 1)):
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        component.append(neighbor)
                        stack.append(neighbor)
            components.append(component)

        component_colors = [
            {grid[row][col] for row, col in component}
            for component in components
        ]
        template_index = next(index for index, colors in enumerate(component_colors)
                              if len(colors) > 1)
        template = components[template_index]
        rows = [row for row, _ in template]
        cols = [col for _, col in template]
        top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)

        uniform_colors = [next(iter(colors)) for colors in component_colors
                          if len(colors) == 1]
        uniform_counts = {}
        for color in uniform_colors:
            uniform_counts[color] = uniform_counts.get(color, 0) + 1
        base_color = None
        for color in uniform_counts:
            if base_color is None or uniform_counts[color] > uniform_counts[base_color]:
                base_color = color

        adjacency = {}
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                color = grid[row][col]
                adjacency.setdefault(color, set())
                for next_row, next_col in ((row + 1, col), (row, col + 1)):
                    if next_row <= bottom and next_col <= right:
                        other = grid[next_row][next_col]
                        if color != other:
                            adjacency[color].add(other)
                            adjacency.setdefault(other, set()).add(color)
        distances = {base_color: 0}
        queue = [base_color]
        position = 0
        while position < len(queue):
            color = queue[position]
            position += 1
            for other in adjacency[color]:
                if other not in distances:
                    distances[other] = distances[color] + 1
                    queue.append(other)
        inner_color = None
        for color in distances:
            if inner_color is None or distances[color] > distances[inner_color]:
                inner_color = color
        inner_cells = [(row, col) for row, col in template
                       if grid[row][col] == inner_color]
        inner_rows = [row for row, _ in inner_cells]
        inner_cols = [col for _, col in inner_cells]
        inner_top, inner_bottom = min(inner_rows), max(inner_rows)
        inner_left, inner_right = min(inner_cols), max(inner_cols)

        source = [row[left:right + 1] for row in grid[top:bottom + 1]]
        source_height = bottom - top + 1
        source_width = right - left + 1
        rows_before = inner_top - top
        rows_after = bottom - inner_bottom
        cols_before = inner_left - left
        cols_after = right - inner_right
        output = [row[:] for row in grid]
        for index, component in enumerate(components):
            if index == template_index or component_colors[index] != {base_color}:
                continue
            target_rows = [row for row, _ in component]
            target_cols = [col for _, col in component]
            target_top, target_bottom = min(target_rows), max(target_rows)
            target_left, target_right = min(target_cols), max(target_cols)
            target_height = target_bottom - target_top + 1
            target_width = target_right - target_left + 1
            for row in range(target_height):
                if row < rows_before:
                    source_row = row
                elif row >= target_height - rows_after:
                    source_row = source_height - (target_height - row)
                else:
                    source_row = rows_before
                for col in range(target_width):
                    if col < cols_before:
                        source_col = col
                    elif col >= target_width - cols_after:
                        source_col = source_width - (target_width - col)
                    else:
                        source_col = cols_before
                    output[target_top + row][target_left + col] = source[source_row][source_col]
    return output
