def main():
    user_input = str(input("Input: "))
    print(omit_vowels(user_input))

def omit_vowels(text):

    vowels = "aeiouAEIOU"

    for vowel in vowels:
        text = text.replace(vowel, "")

    return text

main()


