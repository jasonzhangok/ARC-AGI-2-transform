def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set()
    for row in grid:
        for color in row:
            if color != 0:
                colors.add(color)
    ordered_colors = sorted(colors)
    perimeters = {}

    for color in ordered_colors:
        cells = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] == color:
                    cells.append((row, col))
        top = min(row for row, col in cells)
        bottom = max(row for row, col in cells)
        left = min(col for row, col in cells)
        right = max(col for row, col in cells)
        perimeter = set()
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if row == top or row == bottom or col == left or col == right:
                    perimeter.add((row, col))
        perimeters[color] = perimeter

    above = {color: set() for color in ordered_colors}
    indegree = {color: 0 for color in ordered_colors}
    for first_index in range(len(ordered_colors)):
        first = ordered_colors[first_index]
        for second_index in range(first_index + 1, len(ordered_colors)):
            second = ordered_colors[second_index]
            first_visible = 0
            second_visible = 0
            for row, col in perimeters[first] & perimeters[second]:
                if grid[row][col] == first:
                    first_visible += 1
                elif grid[row][col] == second:
                    second_visible += 1
            if first_visible > second_visible:
                above[second].add(first)
            elif second_visible > first_visible:
                above[first].add(second)

    for lower in ordered_colors:
        for upper in above[lower]:
            indegree[upper] += 1

    layer_colors = []
    while len(layer_colors) < len(ordered_colors):
        available = []
        for color in ordered_colors:
            if color not in layer_colors and indegree[color] == 0:
                available.append(color)
        selected = available[0]
        layer_colors.append(selected)
        for upper in above[selected]:
            indegree[upper] -= 1

    output_size = 2 * len(layer_colors) - 1
    output = [[0 for col in range(output_size)] for row in range(output_size)]
    for layer in range(len(layer_colors)):
        color = layer_colors[layer]
        far = output_size - 1 - layer
        for position in range(layer, far + 1):
            output[layer][position] = color
            output[far][position] = color
            output[position][layer] = color
            output[position][far] = color

    return output
