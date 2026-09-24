
import sys

from checkmate import checkmate


def main():
    arguments = sys.argv[1:]
    explain = "--explain" in arguments
    paths = [argument for argument in arguments if argument != "--explain"]

    if not paths:
        print("Error")
        return

    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as file:
                board = file.read()
        except (OSError, UnicodeError):
            print("Error")
            continue
        checkmate(board, explain=explain)


if __name__ == "__main__":
    main()
