def transform(grid):
    """Replace each nonzero cell by the input pattern and each zero by zeros."""
    if not grid:
        output = []
    else:
        block_width = len(grid[0])
        output = []
        for mask_row in grid:
            for pattern_row in grid:
                output_row = []
                for cell in mask_row:
                    block = pattern_row if cell != 0 else [0] * block_width
                    output_row.extend(block)
                output.append(output_row)
        output = output
    return output
