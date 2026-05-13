def main():
    user_input = (str(input("What do you wish to input and convert? ")))
    print(convert(user_input))

def convert(faces):
    faces = faces.replace(":)", "🙂").replace(":(", "🙁")
    return faces

main()
