def transform(grid):
    height = len(grid)
    width = len(grid[0])
    colors = set()
    for row in grid:
        for color in row:
            if color != 0:
                colors.add(color)

    structure_color = 0
    best_score = -1
    for color in colors:
        score = 0
        for row in range(height - 1):
            for col in range(width - 1):
                if grid[row][col] == color and grid[row + 1][col] == color and grid[row][col + 1] == color and grid[row + 1][col + 1] == color:
                    score += 1
        if score > best_score:
            best_score = score
            structure_color = color

    output_color = 0
    for color in colors:
        if color != structure_color:
            output_color = color

    square_sizes = [[0 for col in range(width)] for row in range(height)]
    block_size = 0
    structure_rows = []
    structure_cols = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == structure_color:
                structure_rows.append(row)
                structure_cols.append(col)
                square_sizes[row][col] = 1
                if row > 0 and col > 0:
                    square_sizes[row][col] += min(square_sizes[row - 1][col], square_sizes[row][col - 1], square_sizes[row - 1][col - 1])
                if square_sizes[row][col] > block_size:
                    block_size = square_sizes[row][col]

    top = min(structure_rows)
    left = min(structure_cols)
    output = [[0 for col in range(3)] for row in range(3)]
    for lattice_row in range(3):
        for lattice_col in range(3):
            occupied = True
            for row_offset in range(block_size):
                for col_offset in range(block_size):
                    row = top + lattice_row * block_size + row_offset
                    col = left + lattice_col * block_size + col_offset
                    if row >= height or col >= width or grid[row][col] != structure_color:
                        occupied = False
            if occupied:
                output[lattice_row][lattice_col] = output_color

    return output
