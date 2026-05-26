Food_data = {

    "apple": 130,
    "avocado": 50,
    "banana": 100,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "lemon": 15,
    "lime": 20,
    "lectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
    "kiwifruit": 90,
}

while True:
    user_input = str(input("Item: "))
    user_input = user_input.strip().lower()

    if user_input in Food_data:
        print(f"Calories: {Food_data[user_input]}", sep=",")
    else:
        print("")

    break


