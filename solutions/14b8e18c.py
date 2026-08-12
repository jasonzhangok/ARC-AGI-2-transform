from collections import Counter, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    output = [row[:] for row in grid]
    seen = set()

    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col] == background or (start_row, start_col) in seen:
                continue
            color = grid[start_row][start_col]
            queue = deque([(start_row, start_col)])
            seen.add((start_row, start_col))
            component = set()
            while queue:
                row, col = queue.popleft()
                component.add((row, col))
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    y, x = row + dr, col + dc
                    if (0 <= y < height and 0 <= x < width and
                            grid[y][x] == color and (y, x) not in seen):
                        seen.add((y, x))
                        queue.append((y, x))

            top = min(r for r, _ in component)
            bottom = max(r for r, _ in component)
            left = min(c for _, c in component)
            right = max(c for _, c in component)
            if bottom - top != right - left or top == bottom:
                continue
            border = {
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if r in (top, bottom) or c in (left, right)
            }
            filled = {
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
            }
            if component not in (border, filled):
                continue
            candidates = [
                (top - 1, left), (top, left - 1),
                (top - 1, right), (top, right + 1),
                (bottom + 1, left), (bottom, left - 1),
                (bottom + 1, right), (bottom, right + 1),
            ]
            for row, col in candidates:
                if 0 <= row < height and 0 <= col < width and grid[row][col] == background:
                    output[row][col] = 2
    return output
