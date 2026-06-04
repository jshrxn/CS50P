import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        correct = False

        for _ in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                guess = None

            if guess == answer:
                score += 1
                correct = True
                break
            else:
                print("EEE")

        if not correct:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
