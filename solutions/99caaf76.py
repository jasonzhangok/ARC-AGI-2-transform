def transform(grid):
    height = len(grid)
    width = len(grid[0])
    counts = {}
    for row in grid:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    background = max(counts, key=counts.get)
    output = [[background for col in range(width)] for row in range(height)]

    patterns = [
        ({(0, 0), (1, 1), (1, 2), (2, 0)}, "left"),
        ({(0, 2), (1, 0), (1, 1), (2, 2)}, "right"),
        ({(0, 0), (0, 2), (1, 1), (2, 1)}, "top"),
        ({(0, 1), (1, 1), (2, 0), (2, 2)}, "bottom"),
    ]
    for scaffold_row in range(height - 2):
        for scaffold_col in range(width - 2):
            for mask, orientation in patterns:
                matches = True
                for row_offset in range(3):
                    for col_offset in range(3):
                        expected = 1 if (row_offset, col_offset) in mask else background
                        if grid[scaffold_row + row_offset][scaffold_col + col_offset] != expected:
                            matches = False
                if not matches:
                    continue

                if orientation == "left":
                    motif_row = scaffold_row
                    motif_col = scaffold_col
                    payload_row = scaffold_row
                    payload_col = scaffold_col + 3
                elif orientation == "right":
                    motif_row = scaffold_row
                    motif_col = scaffold_col - 3
                    payload_row = scaffold_row
                    payload_col = scaffold_col - 3
                elif orientation == "top":
                    motif_row = scaffold_row
                    motif_col = scaffold_col
                    payload_row = scaffold_row + 3
                    payload_col = scaffold_col
                else:
                    motif_row = scaffold_row - 3
                    motif_col = scaffold_col
                    payload_row = scaffold_row - 3
                    payload_col = scaffold_col

                if not (
                    0 <= payload_row <= height - 3
                    and 0 <= payload_col <= width - 3
                ):
                    continue
                payload_has_color = False
                for row_offset in range(3):
                    for col_offset in range(3):
                        if grid[payload_row + row_offset][payload_col + col_offset] != background:
                            payload_has_color = True
                if not payload_has_color:
                    continue

                if orientation in ("left", "right"):
                    target_motif_row = motif_row
                    target_motif_col = width - 6 if motif_col == 0 else 0
                else:
                    target_motif_row = height - 6 if motif_row == 0 else 0
                    target_motif_col = motif_col

                scaffold_relative_row = scaffold_row - motif_row
                scaffold_relative_col = scaffold_col - motif_col
                for row_offset in range(3):
                    for col_offset in range(3):
                        value = grid[scaffold_row + row_offset][scaffold_col + col_offset]
                        if value != background:
                            output[
                                target_motif_row + scaffold_relative_row + row_offset
                            ][
                                target_motif_col + scaffold_relative_col + col_offset
                            ] = value

                payload_relative_row = payload_row - motif_row
                payload_relative_col = payload_col - motif_col
                for row_offset in range(3):
                    for col_offset in range(3):
                        value = grid[payload_row + 2 - row_offset][payload_col + 2 - col_offset]
                        if value != background:
                            output[
                                target_motif_row + payload_relative_row + row_offset
                            ][
                                target_motif_col + payload_relative_col + col_offset
                            ] = value
    return output
