from collections import Counter, deque


def transform(grid):
    h, w = len(grid), len(grid[0])
    marker = next((r, c) for r in range(h) for c in range(w) if grid[r][c] == 8)
    q = deque([marker]); seen = {marker}; cells = []
    while q:
        r, c = q.popleft(); cells.append((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < h and 0 <= nc < w and grid[nr][nc] != 0
                    and (nr, nc) not in seen):
                seen.add((nr, nc)); q.append((nr, nc))
    color = Counter(grid[r][c] for r, c in cells if grid[r][c] != 8).most_common(1)[0][0]
    r0, r1 = min(r for r, _ in cells), max(r for r, _ in cells)
    c0, c1 = min(c for _, c in cells), max(c for _, c in cells)
    return [[color if grid[r][c] == 8 else grid[r][c]
             for c in range(c0, c1 + 1)] for r in range(r0, r1 + 1)]
