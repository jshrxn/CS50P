import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = re.compile(
        r"^(0?[1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to (0?[1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    )

    match = pattern.search(s)

    if not match:
        raise ValueError

    start_hour = int(match.group(1))
    start_minute = match.group(2) if match.group(2) else "00"
    start_period = match.group(3)

    end_hour = int(match.group(4))
    end_minute = match.group(5) if match.group(5) else "00"
    end_period = match.group(6)

    # Convert start time
    if start_period == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12

    # Convert end time
    if end_period == "AM":
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12

    return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"


if __name__ == "__main__":
    main()
