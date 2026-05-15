x = str(input("Greeting: "))

x = x.strip()

if x.startswith("Hello"):
    print("$0")

elif x.lower().startswith("h"):
    print("$20")

else:
    print("$100")
