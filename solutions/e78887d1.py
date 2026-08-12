def transform(grid):
    height = len(grid)
    width = len(grid[0])
    panels = []
    panel_start = None
    for row in range(height):
        if any((value != 0 for value in grid[row])):
            if panel_start is None:
                panel_start = row
        elif panel_start is not None:
            panels.append(grid[panel_start:row])
            panel_start = None
    if panel_start is not None:
        panels.append(grid[panel_start:height])
    if not panels:
        output = [row[:] for row in grid]
    else:
        panel = panels[-1]
        slot_count = (width + 1) // 4
        colors = []
        for slot in range(slot_count):
            color = 0
            for row in range(3):
                for offset in range(3):
                    value = panel[row][4 * slot + offset]
                    if value != 0:
                        color = value
            colors.append(color)
        output = [[0 for _ in range(width)] for _ in range(3)]
        for slot in range(slot_count):
            source_slot = (slot + 1) % slot_count
            for row in range(3):
                for offset in range(3):
                    if panel[row][4 * source_slot + offset] != 0:
                        output[row][4 * slot + offset] = colors[slot]
        output = output
    return output
