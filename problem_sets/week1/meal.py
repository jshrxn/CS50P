def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("breakfast time")

    elif 12 <= converted_time <= 13:
        print("lunch time")

    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    time = time.strip().lower()

    if "a.m." in time or "p.m." in time:

        clock_time, period = time.split()

        hours, minutes = clock_time.split(":")
        hours = float(hours)
        minutes = float(minutes)

        if period == "p.m." and hours != 12:
            hours += 12

        if period == "a.m." and hours == 12:
            hours = 0

        return hours + minutes / 60

    else:
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)

        return hours + minutes / 60


if __name__ == "__main__":
    main()
