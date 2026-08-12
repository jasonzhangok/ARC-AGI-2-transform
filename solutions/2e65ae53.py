def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            if color != 0:
                counts[color] = counts.get(color, 0) + 1
    frame_color = max(counts, key=counts.get)

    seen = set()
    rooms = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == frame_color or (row, col) in seen:
                continue

            cells = []
            queue = [(row, col)]
            seen.add((row, col))
            touches_edge = False
            index = 0
            while index < len(queue):
                current_row, current_col = queue[index]
                index += 1
                cells.append((current_row, current_col))
                if (current_row in (0, height - 1)
                        or current_col in (0, width - 1)):
                    touches_edge = True
                for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col
                    if (0 <= next_row < height and 0 <= next_col < width
                            and grid[next_row][next_col] != frame_color
                            and (next_row, next_col) not in seen):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))

            if not touches_edge:
                rooms.append({
                    "cells": cells,
                    "top": min(point[0] for point in cells),
                    "bottom": max(point[0] for point in cells),
                    "left": min(point[1] for point in cells),
                    "right": max(point[1] for point in cells),
                })

    roles = {}
    role_colors = {}
    for room_index in range(len(rooms)):
        room = rooms[room_index]
        has_left = False
        has_right = False
        has_above = False
        has_below = False
        for other_index in range(len(rooms)):
            if other_index == room_index:
                continue
            other = rooms[other_index]
            if room["top"] == other["top"] and room["bottom"] == other["bottom"]:
                if other["right"] + 2 == room["left"]:
                    has_left = True
                if room["right"] + 2 == other["left"]:
                    has_right = True
            if room["left"] == other["left"] and room["right"] == other["right"]:
                if other["bottom"] + 2 == room["top"]:
                    has_above = True
                if room["bottom"] + 2 == other["top"]:
                    has_below = True

        role = None
        if has_right and has_below:
            role = "top_left"
        elif has_left and has_below:
            role = "top_right"
        elif has_right and has_above:
            role = "bottom_left"
        elif has_left and has_above:
            role = "bottom_right"
        roles[room_index] = role

        sample_colors = set()
        for cell_row, cell_col in room["cells"]:
            color = grid[cell_row][cell_col]
            if color not in (0, frame_color):
                sample_colors.add(color)
        if role is not None and len(sample_colors) == 1:
            for color in sample_colors:
                role_colors[role] = color

    output = [row[:] for row in grid]
    for room_index in range(len(rooms)):
        role = roles[room_index]
        if role not in role_colors:
            continue
        fill_color = role_colors[role]
        for row, col in rooms[room_index]["cells"]:
            if grid[row][col] == 0:
                output[row][col] = fill_color

    return output
