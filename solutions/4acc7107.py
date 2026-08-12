def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = []
    for row in grid:
        for value in row:
            if value != 0 and value not in colors:
                colors.append(value)

    objects = {}
    for color in colors:
        seen = set()
        components = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                cells = []
                frontier = [(row, col)]
                seen.add((row, col))
                index = 0
                while index < len(frontier):
                    current_row, current_col = frontier[index]
                    index += 1
                    cells.append((current_row, current_col))
                    for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        next_row = current_row + delta_row
                        next_col = current_col + delta_col
                        if (0 <= next_row < height and 0 <= next_col < width
                                and grid[next_row][next_col] == color
                                and (next_row, next_col) not in seen):
                            seen.add((next_row, next_col))
                            frontier.append((next_row, next_col))
                min_row = min(cell[0] for cell in cells)
                max_row = max(cell[0] for cell in cells)
                min_col = min(cell[1] for cell in cells)
                max_col = max(cell[1] for cell in cells)
                components.append({
                    "cells": cells,
                    "min_row": min_row,
                    "max_row": max_row,
                    "min_col": min_col,
                    "max_col": max_col,
                    "area": len(cells),
                    "height": max_row - min_row + 1,
                    "width": max_col - min_col + 1,
                })
        objects[color] = components

    left_color = colors[0]
    leftmost_col = width
    for color in colors:
        color_left = width
        for component in objects[color]:
            if component["min_col"] < color_left:
                color_left = component["min_col"]
        if color_left < leftmost_col:
            leftmost_col = color_left
            left_color = color
    right_color = colors[0]
    for color in colors:
        if color != left_color:
            right_color = color

    left_objects = objects[left_color]
    right_objects = objects[right_color]
    best_cost = None
    best_swap = 0
    for axis in (0, 1):
        for swap in (0, 1):
            cost = 0
            for index in range(2):
                other_index = index if swap == 0 else 1 - index
                if axis == 0:
                    left_center = (left_objects[index]["min_row"]
                                   + left_objects[index]["max_row"])
                    right_center = (right_objects[other_index]["min_row"]
                                    + right_objects[other_index]["max_row"])
                else:
                    left_center = (left_objects[index]["min_col"]
                                   + left_objects[index]["max_col"])
                    right_center = (right_objects[other_index]["min_col"]
                                    + right_objects[other_index]["max_col"])
                cost += abs(left_center - right_center)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_swap = swap

    pairs = []
    for index in range(2):
        other_index = index if best_swap == 0 else 1 - index
        pairs.append((left_objects[index], right_objects[other_index]))
    if (pairs[0][0]["area"] + pairs[0][1]["area"]
            > pairs[1][0]["area"] + pairs[1][1]["area"]):
        pairs[0], pairs[1] = pairs[1], pairs[0]

    output = [[0 for col in range(width)] for row in range(height)]
    left_group_width = 0
    for component in left_objects:
        if component["width"] > left_group_width:
            left_group_width = component["width"]
    group_starts = (0, left_group_width + 1)

    for side in range(2):
        top_object = pairs[0][side]
        bottom_object = pairs[1][side]
        bottom_start_row = height - bottom_object["height"]
        top_start_row = bottom_start_row - 1 - top_object["height"]
        start_col = group_starts[side]
        color = left_color if side == 0 else right_color
        for source_row, source_col in top_object["cells"]:
            target_row = top_start_row + source_row - top_object["min_row"]
            target_col = start_col + source_col - top_object["min_col"]
            output[target_row][target_col] = color
        for source_row, source_col in bottom_object["cells"]:
            target_row = bottom_start_row + source_row - bottom_object["min_row"]
            target_col = start_col + source_col - bottom_object["min_col"]
            output[target_row][target_col] = color

    return output
