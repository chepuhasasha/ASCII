"""Utilities for converting images to ASCII art."""

from PIL import Image

# Mapping of brightness thresholds to characters.
ASCII_MAP = [
    (50, " "),
    (100, "░"),
    (150, "▒"),
    (200, "▓"),
    (256, "█"),
]


def _char_for_brightness(value: int) -> str:
    """Return a character for the given brightness value."""
    for threshold, char in ASCII_MAP:
        if value < threshold:
            return char
    return ASCII_MAP[-1][1]


def image_to_ascii(path: str, width: int = 100, height: int = 40) -> str:
    """Convert an image to ASCII art.

    Args:
        path: Path to the image file.
        width: Width of the output in characters.
        height: Height of the output in characters.

    Returns:
        A string containing the ASCII art.
    """
    img = Image.open(path).convert("RGB")
    resized = img.resize((width, height), Image.ANTIALIAS)

    lines = []
    for y in range(height):
        line_chars = []
        for x in range(width):
            pixel = resized.getpixel((x, y))
            brightness = sum(pixel) // 3
            line_chars.append(_char_for_brightness(brightness))
        lines.append("".join(line_chars))
    return "\n".join(lines)


