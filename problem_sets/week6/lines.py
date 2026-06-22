import sys

def main():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            count = 0

            for line in file:
                stripped = line.strip()

                if stripped == "":
                    continue

                if stripped.startswith("#"):
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
