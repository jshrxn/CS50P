import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(input_file, "r", newline="") as infile, \
             open(output_file, "w", newline="") as outfile:

            reader = csv.DictReader(infile)

            writer = csv.DictWriter(
                outfile,
                fieldnames=["first", "last", "house"]
            )

            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(",")

                writer.writerow({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"].strip()
                })

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
