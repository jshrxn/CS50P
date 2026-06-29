import sys
import os
from PIL import Image, ImageOps


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = (".jpg", ".jpeg", ".png")

    if not input_file.lower().endswith(valid_extensions):
        sys.exit("Invalid input")

    if not output_file.lower().endswith(valid_extensions):
        sys.exit("Invalid output")

    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(input_file) as photo, Image.open("shirt.png") as shirt:

            photo = ImageOps.fit(photo, shirt.size)

            photo.paste(shirt, shirt)

            photo.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
