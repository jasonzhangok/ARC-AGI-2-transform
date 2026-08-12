def transform(grid):
    """Tile rows three times across in original, mirrored, original bands."""
    original_band = [row * 3 for row in grid]
    mirrored_band = [list(reversed(row)) * 3 for row in grid]
    return original_band + mirrored_band + original_band
