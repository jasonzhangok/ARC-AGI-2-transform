def transform(grid):
    height = len(grid)
    width = len(grid[0])
    result = [row[:] for row in grid]
    frames = []

    for top in range(height - 2):
        for bottom in range(top + 2, height):
            for left in range(width - 2):
                color = grid[top][left]
                if color == 0:
                    continue
                for right in range(left + 2, width):
                    if not all(grid[top][col] == color and grid[bottom][col] == color for col in range(left, right + 1)):
                        continue
                    if not all(grid[row][left] == color and grid[row][right] == color for row in range(top + 1, bottom)):
                        continue
                    if not all(grid[row][col] == 0 for row in range(top + 1, bottom) for col in range(left + 1, right)):
                        continue
                    frames.append((top, bottom, left, right, color))

    sources = []
    for top, bottom, left, right, color in frames:
        perimeter = 2 * (bottom - top + right - left)
        occurrences = 0
        for row in grid:
            occurrences += row.count(color)
        if occurrences == perimeter:
            sources.append((top, bottom, left, right, color))

    if len(sources) == 1:
        top, bottom, left, right, color = sources[0]
        frame_height = bottom - top + 1
        frame_width = right - left + 1
        targets = []
        for row in range(height - frame_height + 1):
            for col in range(width - frame_width + 1):
                if row == top and col == left:
                    continue
                if not all(grid[y][x] == 0 for y in range(row + 1, row + frame_height - 1) for x in range(col + 1, col + frame_width - 1)):
                    continue
                target_bottom = row + frame_height - 1
                target_right = col + frame_width - 1
                contained_in_frame = False
                for frame_top, frame_bottom, frame_left, frame_right, frame_color in frames:
                    if (frame_top <= row and target_bottom <= frame_bottom
                            and frame_left <= col and target_right <= frame_right):
                        contained_in_frame = True
                if not contained_in_frame:
                    targets.append((row, col))
        if len(targets) == 1:
            row, col = targets[0]
            for x in range(col, col + frame_width):
                result[row][x] = color
                result[row + frame_height - 1][x] = color
            for y in range(row + 1, row + frame_height - 1):
                result[y][col] = color
                result[y][col + frame_width - 1] = color
    output = result
    return output
