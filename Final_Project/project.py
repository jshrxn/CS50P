import math
import sys

class Password:
    def __init__(self, password):
       self.password = password
       self.password_length = 0
       self.uppercase_count = 0
       self.lowercase_count = 0
       self.digit_count = 0
       self.symbol_count = 0

       # To analyze the password immediately so the object's attributes are populated as soon as it is created.
       self.analyze()

    def analyze(self):
        self.password_length = len(self.password)
        self.uppercase_count = 0
        self.lowercase_count = 0
        self.digit_count = 0
        self.symbol_count = 0

        for char in self.password:
            if char.isupper():
                self.uppercase_count += 1
            if char.islower():
                self.lowercase_count += 1
            if char.isdigit():
                self.digit_count += 1
            if not char.isalnum():
                self.symbol_count += 1

class PasswordAnalyzer:
    def __init__(self, password_obj):
        # To store the Password object so the analyzer can access its previously calculated characteristics.
        self.password = password_obj

    def character_pool(self):
        pool = 0

        # To add the size of each character set actually used by the password.
        # Uppercase and lowercase letters each have 26 possible characters.
        # 10 possible digits and 32 possible symbols
        if self.password.lowercase_count:
            pool += 26
        if self.password.uppercase_count:
            pool += 26
        if self.password.digit_count:
            pool += 10
        if self.password.symbol_count:
            pool += 32

        return pool

    def search_space(self):
        pool = self.character_pool()

        # Assuming every character position can contain any character from the calculated pool.
        return pool ** self.password.password_length


    def entropy(self):
        pool = self.character_pool()

        # Shannon-style maximum entropy for a password of this length under the assumed character pool.
        return self.password.password_length * math.log2(pool)

    def strength_rating(self):
        entropy = self.entropy()

        if entropy < 28:
            return "Weak"
        elif entropy < 50:
            return "Moderate"
        elif entropy < 80:
            return "Strong"
        else:
            return "Excellent"

    def crack_time(self):
        # Simplified assumption: one million guesses are attempted per second.
        guesses_per_second = 1000000

        return self.search_space() / guesses_per_second

    def formatted_crack_time(self) -> str:
        seconds = self.crack_time()

        # Uses approximate average month/year lengths for human-readable output.
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            return f"{seconds / 60:.2f} minutes"
        elif seconds < 86400:
            return f"{seconds / 3600:.2f} hours"
        elif seconds < 2629800:
            return f"{seconds / 86400:.2f} days"
        elif seconds < 31557600:
            return f"{seconds / 2629800:.2f} months"
        else:
            return f"{seconds / 31557600:.2f} years"

    def report(self):
        print("-------------------------------------------------")
        print("             PASSWORD CHARACTERISTICS            ")
        print("-------------------------------------------------")

        print(f"Password length: {self.password.password_length}")
        print(f"Uppercase count: {self.password.uppercase_count}")
        print(f"Lowercase count: {self.password.lowercase_count}")
        print(f"Digit count: {self.password.digit_count}")
        print(f"Symbol count: {self.password.symbol_count}")

        print("-------------------------------------------------")
        print("               SECURITY ANALYSIS                 ")
        print("-------------------------------------------------")

        print(f"Character pool: {self.character_pool()}")
        print(f"Search space: {self.search_space():.2e}")
        print(f"Entropy: {self.entropy():.2f} bits")
        print(f"Strength rating: {self.strength_rating()}")
        print(f"Crack time: {self.formatted_crack_time()}")


def main():

    print("=================================================")
    print("               PASSWORD ANALYZER                 ")
    print("=================================================")

    user_password = input("Password: ")

    if not user_password.strip():
        sys.exit("Input cannot be empty or whitespaces only")


    password_obj = Password(user_password)

    analyzer = PasswordAnalyzer(password_obj)

    analyzer.report()


if __name__ == "__main__":
    main()







