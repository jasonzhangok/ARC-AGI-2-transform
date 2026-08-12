def transform(grid: list[list[int]]) -> list[list[int]]:
    """Expand the input bar into ascending then descending serialized bars."""
    if not grid or not grid[0]:
        return [row[:] for row in grid]

    width = len(grid[0])
    colored = [cell for row in grid for cell in row if cell != 0]
    if not colored:
        return [row[:] for row in grid]

    color = colored[0]
    size = len(colored)
    sequence: list[int] = []
    run_lengths = list(range(1, size + 1)) + list(range(size - 1, 0, -1))
    for run_length in run_lengths:
        sequence.extend([color] * run_length)
        sequence.append(0)

    sequence.extend([0] * (-len(sequence) % width))
    return [sequence[start:start + width]
            for start in range(0, len(sequence), width)]
