def transform(grid):
    frame_height = len(grid) // 3
    width = len(grid[0])
    first = grid[:frame_height]
    second = grid[frame_height:2 * frame_height]
    template = grid[2 * frame_height:]
    output = [row[:] for row in template]

    for row in range(frame_height):
        changing_colors = {
            first[row][col]
            for col in range(width)
            if first[row][col] != template[row][col]
        } | {
            second[row][col]
            for col in range(width)
            if second[row][col] != template[row][col]
        }
        for color in changing_colors:
            first_positions = [
                col for col in range(width)
                if first[row][col] == color and first[row][col] != template[row][col]
            ]
            second_positions = [
                col for col in range(width)
                if second[row][col] == color and second[row][col] != template[row][col]
            ]
            if not first_positions or not second_positions:
                continue
            next_left = 2 * min(second_positions) - min(first_positions)
            next_right = 2 * max(second_positions) - max(first_positions)
            for col in range(next_left, next_right + 1):
                output[row][col] = color
    return output
