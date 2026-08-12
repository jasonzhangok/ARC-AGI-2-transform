def transform(grid):
    try:
        'Expand the input bar into ascending then descending serialized bars.'
        if not grid or not grid[0]:
            raise StopIteration([row[:] for row in grid])
        width = len(grid[0])
        colored = [cell for row in grid for cell in row if cell != 0]
        if not colored:
            raise StopIteration([row[:] for row in grid])
        color = colored[0]
        size = len(colored)
        sequence: list[int] = []
        run_lengths = list(range(1, size + 1)) + list(range(size - 1, 0, -1))
        for run_length in run_lengths:
            sequence.extend([color] * run_length)
            sequence.append(0)
        sequence.extend([0] * (-len(sequence) % width))
        raise StopIteration([sequence[start:start + width] for start in range(0, len(sequence), width)])
    except StopIteration as _return_signal:
        output = _return_signal.args[0]
    return output
