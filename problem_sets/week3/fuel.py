def fuel_gauge():
    while True:
        user_input = input("Fraction: ").strip()

        try:

            if '/' not in user_input:
                raise ValueError("Missing slash")

            parts = user_input.split('/')
            if len(parts) != 2:
                raise ValueError("Invalid format")

            x_str, y_str = parts[0], parts[1]


            x = int(x_str)
            y = int(y_str)


            if y == 0:
                raise ZeroDivisionError("Denominator cannot be zero")

            if x > y:
                raise ValueError("Numerator cannot be greater than denominator")

            if x < 0:
                raise ValueError("Numerator must be non-negative")


            percentage = round((x / y) * 100)


            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            pass


fuel_gauge()
