from datetime import date, datetime
import sys
import inflect


z = inflect.engine()


class DateCalc:
    def __init__(self, date_obj):
        try:
            self.date_obj = datetime.strptime(date_obj, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError

    def minutes(self):
        today = date.today()
        delta = today - self.date_obj
        return delta.days * 24 * 60

    def words(self):
        return (
            z.number_to_words(self.minutes(), andword="")
            .capitalize()
            + " minutes"
        )


def main():
    try:
        birthday = input("Date of Birth: ")
        calc = DateCalc(birthday)
        print(calc.words())
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
