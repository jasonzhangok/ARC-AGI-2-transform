"""Trace border-originating rays through walls with gaps."""


def transform(grid):
    """Extend border-originating rays, detouring around cyan walls."""
    height = len(grid)
    width = len(grid[0]) if height else 0
    result = [row[:] for row in grid]

    # A state is a ray standing on a non-wall cell, pointing in its travel
    # direction.  Rays that collide with a wall produce two wall-followers.
    pending = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2:
                continue
            if row == 0:
                pending.append((row, col, 1, 0))
            if row == height - 1:
                pending.append((row, col, -1, 0))
            if col == 0:
                pending.append((row, col, 0, 1))
            if col == width - 1:
                pending.append((row, col, 0, -1))

    seen_rays = set()
    seen_followers = set()
    while pending:
        row, col, d_row, d_col = pending.pop()
        ray = (row, col, d_row, d_col)
        if ray in seen_rays:
            continue
        seen_rays.add(ray)

        next_row, next_col = row + d_row, col + d_col
        if not (0 <= next_row < height and 0 <= next_col < width):
            continue
        if grid[next_row][next_col] != 8:
            if result[next_row][next_col] == 0:
                result[next_row][next_col] = 2
            pending.append((next_row, next_col, d_row, d_col))
            continue

        # The wall blocks the forward ray.  On its current side, follow the
        # wall in both perpendicular directions until the first opening; pass
        # through that opening and resume the original direction.
        for side_row, side_col in ((d_col, -d_row), (-d_col, d_row)):
            follow_row, follow_col = row, col
            follower = (follow_row, follow_col, d_row, d_col, side_row, side_col)
            while follower not in seen_followers:
                seen_followers.add(follower)
                follow_row += side_row
                follow_col += side_col
                if not (0 <= follow_row < height and 0 <= follow_col < width):
                    break
                if result[follow_row][follow_col] == 0:
                    result[follow_row][follow_col] = 2
                wall_row = follow_row + d_row
                wall_col = follow_col + d_col
                if not (0 <= wall_row < height and 0 <= wall_col < width):
                    break
                if grid[wall_row][wall_col] != 8:
                    if result[wall_row][wall_col] == 0:
                        result[wall_row][wall_col] = 2
                    pending.append((wall_row, wall_col, d_row, d_col))
                    break
                follower = (follow_row, follow_col, d_row, d_col, side_row, side_col)

    return result
