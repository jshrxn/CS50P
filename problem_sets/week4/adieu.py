import inflect
p = inflect.engine()

name_list = []

while True:
    try:
        name = str(input("Name: ")).strip().title()
        name_list.append(name)

        result = p.join(name_list)

    except EOFError:
        print(f"\nAdieu, adieu, to {result}")
        break


