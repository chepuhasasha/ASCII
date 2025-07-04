"""Utility script to display the generated ASCII art."""


def main() -> None:
    with open("data.txt", "r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    main()
