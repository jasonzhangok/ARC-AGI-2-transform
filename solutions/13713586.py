def transform(grid):
    height, width = (len(grid), len(grid[0]))
    output = [row[:] for row in grid]
    full_row = next((r for r, row in enumerate(grid) if all((value == 5 for value in row))), None)
    if full_row is not None:
        direction = -1 if full_row == height - 1 else 1
        for c in range(width):
            markers = [(r, grid[r][c]) for r in range(height) if grid[r][c] not in (0, 5)]
            markers = [_sort_record_1[2] for _sort_record_1 in sorted(((abs(_sort_item_1[0] - full_row), _sort_index_1, _sort_item_1) for _sort_index_1, _sort_item_1 in enumerate(markers)))]
            previous = full_row
            for position, color in markers:
                for r in range(previous + direction, position + direction, direction):
                    output[r][c] = color
                previous = position
    else:
        full_column = next((c for c in range(width) if all((grid[r][c] == 5 for r in range(height)))))
        direction = -1 if full_column == width - 1 else 1
        for r in range(height):
            markers = [(c, grid[r][c]) for c in range(width) if grid[r][c] not in (0, 5)]
            markers = [_sort_record_2[2] for _sort_record_2 in sorted(((abs(_sort_item_2[0] - full_column), _sort_index_2, _sort_item_2) for _sort_index_2, _sort_item_2 in enumerate(markers)))]
            previous = full_column
            for position, color in markers:
                for c in range(previous + direction, position + direction, direction):
                    output[r][c] = color
                previous = position
    return output
