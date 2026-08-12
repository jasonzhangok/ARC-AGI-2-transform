def transform(grid):
    try:
        if not grid or not grid[0]:
            raise StopIteration([row[:] for row in grid])
        height, width = (len(grid), len(grid[0]))
        output = [row[:] for row in grid]
        separator_rows = [row for row in range(height) if all((value == 0 for value in grid[row]))]
        separator_cols = [col for col in range(width) if all((grid[row][col] == 0 for row in range(height)))]
        _length = height
        _separators = separator_rows
        'Return half-open runs between separator indices.'
        _separators = set(_separators)
        runs = []
        start = None
        for index in range(_length):
            if index in _separators:
                if start is not None:
                    runs.append((start, index))
                    start = None
            elif start is None:
                start = index
        if start is not None:
            runs.append((start, _length))
        _runs_result_1 = runs
        row_runs = _runs_result_1
        _length = width
        _separators = separator_cols
        'Return half-open runs between separator indices.'
        _separators = set(_separators)
        runs = []
        start = None
        for index in range(_length):
            if index in _separators:
                if start is not None:
                    runs.append((start, index))
                    start = None
            elif start is None:
                start = index
        if start is not None:
            runs.append((start, _length))
        _runs_result_2 = runs
        col_runs = _runs_result_2
        separator_row_set = set(separator_rows)
        separator_col_set = set(separator_cols)
        nonzero_interior = {}
        for cell_value in (grid[row][col] for row in range(height) for col in range(width) if row not in separator_row_set and col not in separator_col_set and (grid[row][col] != 0)):
            nonzero_interior[cell_value] = nonzero_interior.get(cell_value, 0) + 1
        if not nonzero_interior:
            raise StopIteration(output)
        background = max(nonzero_interior, key=nonzero_interior.get)
        regions = []
        for row_start, row_end in row_runs:
            for col_start, col_end in col_runs:
                block = [row[col_start:col_end] for row in grid[row_start:row_end]]
                colored_count = sum((value not in (0, background) for row in block for value in row))
                regions.append((row_start, row_end, col_start, col_end, block, colored_count))
        source_candidates = [region for region in regions if region[-1] > 0 and (not any((value == 0 for row in region[4] for value in row)))]
        if len(source_candidates) != 1:
            raise StopIteration(output)
        source = source_candidates[0]
        source_block = source[4]
        source_shape = (len(source_block), len(source_block[0]))
        for row_start, row_end, col_start, col_end, block, _ in regions:
            if (len(block), len(block[0])) != source_shape:
                continue
            if any((value == 0 for row in block for value in row)):
                for local_row, source_row in enumerate(source_block):
                    output[row_start + local_row][col_start:col_end] = source_row[:]
        raise StopIteration(output)
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
