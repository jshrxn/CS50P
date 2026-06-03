import random

while True:
    try:
        n = int(input("Level: "))

        if n < 0:
            continue

        if n >= 0:
            range = random.randint(1, n)
            break

    except ValueError:
        continue

while True:
    try:
        g = int(input("Guess: "))

        if g < 0:
            continue

        if g > 0:
            if g < range:
                print("Too small!")
                continue

            elif g > range:
                print("Too Large!")
                continue

            elif g == range:
                print("Just right!")
                break

    except ValueError:
        continue





