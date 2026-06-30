import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    result = re.search(
        r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$",
        ip
    )

    return result is not None


if __name__ == "__main__":
    main()
