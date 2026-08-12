def transform(grid):
    height = len(grid)
    width = len(grid[0])
    features = []
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            for tangent_row, tangent_col, normal_row, normal_col in ((1, 0, 0, 1), (0, 1, 1, 0)):
                before = (row - tangent_row, col - tangent_col)
                after = (row + tangent_row, col + tangent_col)
                if not (0 <= before[0] < height and 0 <= before[1] < width and (0 <= after[0] < height) and (0 <= after[1] < width)):
                    continue
                boundary_color = grid[before[0]][before[1]]
                if boundary_color == color or grid[after[0]][after[1]] != boundary_color:
                    continue
                for sign in (-1, 1):
                    solid = (row + sign * normal_row, col + sign * normal_col)
                    if not (0 <= solid[0] < height and 0 <= solid[1] < width and (grid[solid[0]][solid[1]] == color)):
                        continue
                    solid_before = (solid[0] - tangent_row, solid[1] - tangent_col)
                    solid_after = (solid[0] + tangent_row, solid[1] + tangent_col)
                    if not (0 <= solid_before[0] < height and 0 <= solid_before[1] < width and (0 <= solid_after[0] < height) and (0 <= solid_after[1] < width)):
                        continue
                    if grid[solid_before[0]][solid_before[1]] == color and grid[solid_after[0]][solid_after[1]] == color:
                        features.append(({(row, col), solid}, frozenset((color, boundary_color))))
    interfaces = {interface for _, interface in features}
    if len(interfaces) < 2:
        output = [row[:] for row in grid]
    else:
        common_colors = set.intersection(*(set(interface) for interface in interfaces))
        region_colors = set.union(*(set(interface) for interface in interfaces)) - common_colors
        output = [row[:] for row in grid]
        for cells, interface in features:
            replacements = region_colors - set(interface)
            if len(replacements) != 1:
                continue
            replacement = next(iter(replacements))
            for row, col in cells:
                output[row][col] = replacement
        output = output
    return output
