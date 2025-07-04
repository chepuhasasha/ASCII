"""Command line interface for generating ASCII art from images."""

import argparse
from pathlib import Path

from ascii_art import image_to_ascii


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate ASCII art from an image")
    parser.add_argument("image", nargs="?", default="1.png", help="Path to the input image")
    parser.add_argument("--width", type=int, default=100, help="Output width in characters")
    parser.add_argument("--height", type=int, default=40, help="Output height in characters")
    parser.add_argument("-o", "--output", help="Optional path to save the ASCII art")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ascii_art = image_to_ascii(args.image, args.width, args.height)

    if args.output:
        path = Path(args.output)
        path.write_text(ascii_art, encoding="utf-8")

    print(ascii_art)


if __name__ == "__main__":
    main()
