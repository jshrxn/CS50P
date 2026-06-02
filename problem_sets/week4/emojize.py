import emoji

while True:

    user_input = str(input("Input: "))

    if ":" not in user_input:
        print("Invalid code")
        continue

    if ":" in user_input:
        result = emoji.emojize(user_input, language='alias')
        print(f"Output: {result}")
        break









