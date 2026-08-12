def transform(grid):
    height = len(grid)
    width = len(grid[0])

    size = 0
    template_top = 0
    template_left = 0
    for top in range(height):
        for left in range(width):
            candidate_size = 1
            while top + candidate_size <= height and left + candidate_size <= width:
                solid = True
                for row in range(top, top + candidate_size):
                    for col in range(left, left + candidate_size):
                        if grid[row][col] == 0:
                            solid = False
                if not solid:
                    break
                if candidate_size > size:
                    size = candidate_size
                    template_top = top
                    template_left = left
                candidate_size += 1

    mappings = {}
    for row in range(height):
        for col in range(width):
            inside_template = (template_top <= row < template_top + size
                               and template_left <= col < template_left + size)
            if grid[row][col] == 0 or inside_template:
                continue
            tile_row = (row - template_top) // size
            tile_col = (col - template_left) // size
            local_row = (row - template_top) % size
            local_col = (col - template_left) % size
            source_row = local_row if tile_row % 2 == 0 else size - 1 - local_row
            source_col = local_col if tile_col % 2 == 0 else size - 1 - local_col
            source_color = grid[template_top + source_row][template_left + source_col]
            mappings[(tile_row, tile_col, source_color)] = grid[row][col]

    output = [row[:] for row in grid]
    for tile_row, tile_col, source_color in mappings:
        target_color = mappings[(tile_row, tile_col, source_color)]
        for local_row in range(size):
            for local_col in range(size):
                source_row = local_row if tile_row % 2 == 0 else size - 1 - local_row
                source_col = local_col if tile_col % 2 == 0 else size - 1 - local_col
                row = template_top + tile_row * size + local_row
                col = template_left + tile_col * size + local_col
                if (0 <= row < height and 0 <= col < width
                        and grid[template_top + source_row][template_left + source_col] == source_color):
                    output[row][col] = target_color
    return output
