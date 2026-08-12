

def transform(grid):
    height, width = len(grid), len(grid[0])
    eights = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 8}
    top, bottom = min(r for r, _ in eights), max(r for r, _ in eights)
    left, right = min(c for _, c in eights), max(c for _, c in eights)
    middle_row = (top + bottom) / 2
    middle_col = (left + right) / 2
    output = [[0, 0], [0, 0]]
    seen = set()
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            color = grid[row][col]
            if color in (0, 8) or (row, col) in seen:
                continue
            queue = list([(row, col)])
            seen.add((row, col))
            component = []
            while queue:
                y, x = queue.pop(0)
                component.append((y, x))
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    point = (y + dy, x + dx)
                    if (point not in seen and top <= point[0] <= bottom and left <= point[1] <= right
                            and grid[point[0]][point[1]] == color):
                        seen.add(point)
                        queue.append(point)
            center_row = sum(y for y, _ in component) / len(component)
            center_col = sum(x for _, x in component) / len(component)
            output[int(center_row > middle_row)][int(center_col > middle_col)] = color
    return output
