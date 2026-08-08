# Password Strength Analyzer

#### Video Demo: https://youtu.be/ZnmF4hj50ec

#### Description:

Password Strength Analyzer is a Python command-line program that analyzes a password and estimates how resistant it may be to a simple brute-force attack.

I originally became interested in this project because I worked on a mathematical research project involving password resistance before taking CS50P. That project made me interested in how concepts such as probability, search spaces, and entropy can be applied to something practical. For my CS50P final project, I wanted to revisit that idea at a level that I could actually implement and understand in Python.

The program asks the user for a password and analyzes its basic characteristics. It determines the password's length and counts how many uppercase letters, lowercase letters, digits, and symbols it contains. It then uses those characteristics to estimate the size of the character pool and the number of possible combinations that would have to be searched in a brute-force scenario.

The program also calculates an approximate entropy value in bits, assigns the password a simple strength rating, and estimates how long a brute-force search could take under a fixed assumption of 1,000,000 guesses per second. The estimated time is then formatted into a more readable unit such as seconds, minutes, hours, days, months, or years.

## How It Works

The project is organized around two classes: `Password` and `PasswordAnalyzer`.

### `Password`

The `Password` class is responsible for storing the password and analyzing its basic characteristics.

When a `Password` object is created, it receives the password as an argument and immediately analyzes it. The program counts:

* Password length
* Uppercase characters
* Lowercase characters
* Digits
* Symbols

For example, a password such as `Hello123` contains:

* 8 characters
* 1 uppercase letter
* 4 lowercase letters
* 3 digits
* 0 symbols

Keeping these characteristics inside the `Password` object allows the analysis class to use the results without having to repeatedly inspect the original password.

### `PasswordAnalyzer`

The `PasswordAnalyzer` class receives a `Password` object and performs the mathematical analysis.

First, the program estimates the character pool. The current model assumes:

* 26 possible lowercase letters
* 26 possible uppercase letters
* 10 possible digits
* 32 possible symbols

Only character categories that actually appear in the password are included in the pool.

For example, a password containing lowercase letters, uppercase letters, and digits would have an estimated character pool of:

`26 + 26 + 10 = 62`

The program then estimates the brute-force search space using the character pool and password length:

`search space = character pool ^ password length`

The entropy calculation is based on:

`entropy = password length × log2(character pool)`

The resulting entropy is then mapped to one of four simple categories:

* Weak
* Moderate
* Strong
* Excellent

Finally, the estimated search space is divided by the assumed number of guesses per second to produce an estimated brute-force crack time.

## Crack-Time Model

The program currently assumes a constant rate of:

`1,000,000 guesses per second`

This is intentionally a simplified model. Real password-cracking speeds vary significantly depending on the hashing algorithm, hardware, attack method, password-storage system, and whether an attacker is performing an online or offline attack.

Therefore, the crack-time value should be interpreted as a mathematical estimate rather than a prediction of how long a real attacker would actually need.

The program also assumes a simplified character set and does not account for dictionary attacks, leaked passwords, common patterns, keyboard patterns, password reuse, or other techniques that can make real-world passwords easier to guess.

## Project Structure

The project currently consists of:

```text
project/
│
├── project.py
├── test_project.py
└── README.md
└── requirements.txt
```

`project.py` contains the main program and both classes.

`test_project.py` contains pytest tests for the password characteristics and security-analysis calculations.

`README.md` documents the project, its purpose, design, and mathematical model.

`requirements.txt` Contains the project's external Python dependency, `pytest`, which is used to run the automated tests in `test_project.py`. The `math` and `sys` modules used by the project are part of Python's standard library and therefore do not need to be listed.


## Testing

The project uses `pytest` for automated testing.

The tests verify the expected results for a known password, including:

* Password length
* Uppercase count
* Lowercase count
* Digit count
* Symbol count
* Character pool
* Search space
* Entropy
* Strength rating
* Crack-time calculation

The baseline test password is `Hello123`, which provides a useful mixed-character example containing uppercase letters, lowercase letters, and digits.

To run the tests:

```bash
pytest
```

## Running the Program

Make sure Python is installed, then run:

```bash
python project.py
```

The program will prompt:

```text
Password:
```

After entering a password, it displays its characteristics and the resulting security analysis directly in the terminal.

## Design Decisions

One of the main goals of this project was to practice object-oriented programming rather than putting the entire program into one large sequence of functions.

The `Password` class is responsible for **what the password contains**, while the `PasswordAnalyzer` class is responsible for **what those characteristics mean mathematically**.

The `report()` method then brings the results together for the user without requiring `main()` to manually print every individual calculation.

This separation made the project more structured and also gave me practice with passing objects between classes, accessing attributes from another object, and having methods depend on the results of other methods.

## Limitations

This project is primarily an educational mathematical model and should not be treated as a professional password-security tool.

Some important limitations are:

1. The character pool uses simplified fixed character-set sizes.
2. The brute-force model assumes every possible combination is equally likely.
3. The crack-time calculation assumes a constant 1,000,000 guesses per second.
4. Real-world attacks can use dictionaries, leaked password databases, patterns, and other optimizations.
5. The program does not identify whether a password has appeared in a breach.
6. The entropy calculation represents theoretical search-space entropy, not necessarily the true unpredictability of a human-created password.
7. Real cracking speeds depend heavily on the hashing algorithm and hardware.

These limitations are important because a password can have a large theoretical search space while still being predictable if it follows a common pattern.

## What I Learned

This project gave me an opportunity to combine programming with mathematics that I had previously studied in a more theoretical context.

More importantly, it forced me to work with object-oriented programming in an actual project rather than only solving isolated exercises. I had to figure out how to represent a password as an object, how to pass that object into another class, how methods could depend on one another, and how to organize the program so that `main()` mainly handles input and program flow.

I also practiced automated testing with pytest and learned that getting a program to run is only part of the process. The results still need to be tested against known values.

The project is intentionally not a full-scale password auditing system. Instead, it is a relatively small implementation of an idea I was already interested in, rebuilt using the Python programming and software-design skills I developed throughout CS50P.
