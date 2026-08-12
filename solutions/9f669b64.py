def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    background = max(counts, key=counts.get)

    components = []
    seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in seen:
                continue
            color = grid[row][col]
            cells = []
            stack = [(row, col)]
            seen.add((row, col))
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step, col_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (current_row + row_step, current_col + col_step)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] == color
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            min_row = min(cell[0] for cell in cells)
            max_row = max(cell[0] for cell in cells)
            min_col = min(cell[1] for cell in cells)
            max_col = max(cell[1] for cell in cells)
            components.append({
                "cells": cells,
                "color": color,
                "min_row": min_row,
                "max_row": max_row,
                "min_col": min_col,
                "max_col": max_col,
                "height": max_row - min_row + 1,
                "width": max_col - min_col + 1,
            })

    mover_index = None
    movement_axis = None
    for candidate in range(len(components)):
        others = [index for index in range(len(components)) if index != candidate]
        for axis in (0, 1):
            minimum = "min_row" if axis == 0 else "min_col"
            maximum = "max_row" if axis == 0 else "max_col"
            mover_min = components[candidate][minimum]
            mover_max = components[candidate][maximum]
            first = components[others[0]]
            second = components[others[1]]
            if (
                first[maximum] < mover_min
                and mover_max < second[minimum]
            ) or (
                second[maximum] < mover_min
                and mover_max < first[minimum]
            ):
                mover_index = candidate
                movement_axis = axis
                break
        if mover_index is not None:
            break

    mover = components[mover_index]
    outer_indices = [
        index for index in range(len(components)) if index != mover_index
    ]
    perpendicular_size = mover["width"] if movement_axis == 0 else mover["height"]
    barrier_index = None
    for index in outer_indices:
        component = components[index]
        solid = len(component["cells"]) == component["height"] * component["width"]
        span = component["width"] if movement_axis == 0 else component["height"]
        if solid and span > perpendicular_size:
            barrier_index = index
            break
    if barrier_index is None:
        barrier_index = outer_indices[0]
        for index in outer_indices[1:]:
            current_span = (
                components[index]["width"]
                if movement_axis == 0
                else components[index]["height"]
            )
            best_span = (
                components[barrier_index]["width"]
                if movement_axis == 0
                else components[barrier_index]["height"]
            )
            if current_span > best_span:
                barrier_index = index
    pusher_index = next(index for index in outer_indices if index != barrier_index)
    barrier = components[barrier_index]
    pusher = components[pusher_index]

    minimum = "min_row" if movement_axis == 0 else "min_col"
    maximum = "max_row" if movement_axis == 0 else "max_col"
    direction = 1 if pusher[maximum] < mover[minimum] else -1

    output = [row[:] for row in grid]
    for row, col in mover["cells"] + barrier["cells"]:
        output[row][col] = background

    barrier_perpendicular_min = (
        barrier["min_col"] if movement_axis == 0 else barrier["min_row"]
    )
    barrier_perpendicular_size = (
        barrier["width"] if movement_axis == 0 else barrier["height"]
    )
    lower_shift = perpendicular_size // 2
    upper_shift = perpendicular_size - lower_shift
    for row, col in barrier["cells"]:
        perpendicular = col if movement_axis == 0 else row
        local = perpendicular - barrier_perpendicular_min
        shift = -lower_shift if local * 2 < barrier_perpendicular_size else upper_shift
        target_row = row if movement_axis == 0 else row + shift
        target_col = col + shift if movement_axis == 0 else col
        if 0 <= target_row < height and 0 <= target_col < width:
            output[target_row][target_col] = barrier["color"]

    axis_size = mover["height"] if movement_axis == 0 else mover["width"]
    boundary_start = 0
    if direction > 0:
        boundary_start = (height if movement_axis == 0 else width) - axis_size
    for row, col in mover["cells"]:
        if movement_axis == 0:
            target_row = boundary_start + row - mover["min_row"]
            target_col = col
        else:
            target_row = row
            target_col = boundary_start + col - mover["min_col"]
        output[target_row][target_col] = mover["color"]

    return output
