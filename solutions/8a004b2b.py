def transform(grid):
    height = len(grid)
    width = len(grid[0])
    corners = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 4:
                corners.append((row, col))
    crop_top = min(row for row, col in corners)
    crop_bottom = max(row for row, col in corners)
    crop_left = min(col for row, col in corners)
    crop_right = max(col for row, col in corners)

    components = []
    seen = set()
    for row in range(crop_top, crop_bottom + 1):
        for col in range(crop_left, crop_right + 1):
            if grid[row][col] in (0, 4) or (row, col) in seen:
                continue
            color = grid[row][col]
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (current_row + row_step, current_col + col_step)
                    if (
                        crop_top <= neighbor[0] <= crop_bottom
                        and crop_left <= neighbor[1] <= crop_right
                        and grid[neighbor[0]][neighbor[1]] == color
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            components.append({
                "cells": cells,
                "color": color,
                "top": min(cell[0] for cell in cells),
                "left": min(cell[1] for cell in cells),
                "bottom": max(cell[0] for cell in cells),
                "right": max(cell[1] for cell in cells),
            })

    scale = components[0]["bottom"] - components[0]["top"] + 1
    hint_cells = []
    for row in range(height):
        for col in range(width):
            outside = not (
                crop_top <= row <= crop_bottom
                and crop_left <= col <= crop_right
            )
            if outside and grid[row][col] not in (0, 4):
                hint_cells.append((row, col, grid[row][col]))
    hint_top = min(row for row, col, color in hint_cells)
    hint_left = min(col for row, col, color in hint_cells)

    anchor_component = components[0]
    anchor_hint = None
    for row, col, color in hint_cells:
        if color == anchor_component["color"]:
            anchor_hint = (row, col)
            break
    offset_row = (
        anchor_component["top"] - crop_top
        - (anchor_hint[0] - hint_top) * scale
    )
    offset_col = (
        anchor_component["left"] - crop_left
        - (anchor_hint[1] - hint_left) * scale
    )

    output = [
        row[crop_left:crop_right + 1]
        for row in grid[crop_top:crop_bottom + 1]
    ]
    for row, col, color in hint_cells:
        target_top = offset_row + (row - hint_top) * scale
        target_left = offset_col + (col - hint_left) * scale
        for row_offset in range(scale):
            for col_offset in range(scale):
                target_row = target_top + row_offset
                target_col = target_left + col_offset
                if (
                    0 <= target_row < len(output)
                    and 0 <= target_col < len(output[0])
                ):
                    output[target_row][target_col] = color
    return output
