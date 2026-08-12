from collections import Counter, deque


def transform(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    components = []
    while remaining:
        start = remaining.pop()
        component = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (rr, cc) in remaining:
                    remaining.remove((rr, cc))
                    component.add((rr, cc))
                    queue.append((rr, cc))
        components.append(component)

    base = Counter(grid[r][c] for comp in components for r, c in comp).most_common(1)[0][0]
    boxes = []
    for comp in components:
        rows = [r for r, _ in comp]
        cols = [c for _, c in comp]
        boxes.append((min(rows), max(rows), min(cols), max(cols)))
    out_h = boxes[0][1] - boxes[0][0] + 1
    out_w = boxes[0][3] - boxes[0][2] + 1
    result = [[base] * out_w for _ in range(out_h)]
    for top, bottom, left, right in boxes:
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if grid[r][c] != base:
                    result[r - top][c - left] = grid[r][c]
    return result
