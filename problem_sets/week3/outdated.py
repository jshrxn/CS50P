Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        user_input = input("Date: ").strip()

        if "/" in user_input:
            MM, DD, YYYY = user_input.split("/")

            MM = int(MM)
            DD = int(DD)
            YYYY = int(YYYY)

        elif "," in user_input:
            date_part, YYYY = user_input.split(",")

            MM, DD = date_part.strip().split()

            MM = Months.index(MM) + 1
            DD = int(DD)
            YYYY = int(YYYY)

        else:
            continue

        if not (1 <= MM <= 12):
            continue

        if not (1 <= DD <= 31):
            continue

        print(f"{YYYY}-{MM:02d}-{DD:02d}")
        break

    except ValueError:
        continue
