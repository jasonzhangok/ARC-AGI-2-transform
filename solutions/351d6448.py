def transform(grid):
    separators = [r for r, row in enumerate(grid) if all(value == 5 for value in row)]
    cuts = [-1] + separators + [len(grid)]
    panels = [grid[cuts[i] + 1:cuts[i + 1]] for i in range(len(cuts) - 1)]
    height, width = len(panels[0]), len(grid[0])
    result = [[0] * width for _ in range(height)]
    for r in range(height):
        intervals = []
        for panel in panels:
            cells = [c for c, value in enumerate(panel[r]) if value != 0]
            if cells:
                intervals.append((min(cells), max(cells), [panel[r][c] for c in range(min(cells), max(cells) + 1)]))
        if len(intervals) < 2:
            continue
        previous, last = intervals[-2], intervals[-1]
        left = last[0] + last[0] - previous[0]
        right = last[1] + last[1] - previous[1]
        new_width = right - left + 1
        if new_width == len(last[2]):
            values = last[2]
        else:
            color = next(value for value in last[2] if value != 0)
            values = [color] * new_width
        for c, value in enumerate(values, left):
            if 0 <= c < width:
                result[r][c] = value
    return result
