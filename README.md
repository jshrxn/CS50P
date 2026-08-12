# CS50P — Introduction to Programming with Python

My complete coursework and development journey through **Harvard University's CS50P: Introduction to Programming with Python**.

This repository contains my problem sets, exercises, experiments, testing work, and final project developed throughout the course.

> **Status: Completed — August 2026**

---

## About the Course

**CS50P** is Harvard's introduction to programming using Python. The course covers the fundamentals of programming while gradually introducing more advanced concepts through practical problem sets.

For me, this course was more than learning Python syntax. It was my first structured experience with programming as a discipline.

Before starting CS50P, I had only a limited understanding of Python. Throughout the course, I gradually learned how to approach problems, break them into smaller pieces, debug my own code, test programs, work with documentation, and eventually design a complete project.

---

## What I Learned

Throughout the course, I worked with:

* Python fundamentals and syntax
* Variables, expressions, and functions
* Conditionals
* Loops
* Exceptions and input validation
* Libraries and modules
* Unit testing with pytest
* File I/O
* Regular expressions
* Object-oriented programming
* Classes, objects, attributes, and methods
* Command-line programs
* Program architecture and organization
* Debugging and error handling
* Documentation and README writing
* Designing and testing a complete Python project

More importantly, I learned how to approach programming problems rather than simply memorizing syntax.

---

## Course Progress

The repository is organized according to the progression of the course.

### Week 0 — Functions, Variables

Introduced the basic building blocks of Python programming and began developing problem-solving habits.

### Week 1 — Conditionals

Worked with conditional logic and learned how programs make decisions based on input and state.

### Week 2 — Loops

Practiced iteration and learned to translate repetitive processes into program logic.

### Week 3 — Exceptions

Worked with error handling, validation, and making programs respond appropriately to invalid input.

### Week 4 — Libraries

Learned how to use existing Python libraries and integrate functionality written by others into my own programs.

### Week 5 — Unit Tests

Introduced automated testing with pytest and learned the importance of verifying that programs behave as expected.

### Week 6 — File I/O

Worked with reading and writing files and handling data outside of the immediate program execution.

### Week 7 — Regular Expressions

Learned how regular expressions can be used to identify and process structured patterns in text.

### Week 8 — Object-Oriented Programming

Worked with classes and objects and learned how to organize programs around data and behavior.

This was one of the more challenging parts of the course for me, but it also became one of the most valuable concepts to understand.

### Week 9 — Et Cetera

Completed the final portion of the course before moving on to the final project.

---

# Final Project — Password Strength Analyzer

My final project is a command-line **Password Strength Analyzer**.

The project analyzes a password's characteristics and produces a mathematical estimate of its theoretical resistance to a brute-force attack.

The idea was inspired by a mathematical research project I worked on before taking CS50P involving password resistance, probability, and computational analysis. I decided to revisit that idea using the programming and software-design skills I developed during the course.

## What It Does

The program analyzes:

* Password length
* Uppercase characters
* Lowercase characters
* Digits
* Symbols
* Estimated character pool
* Estimated brute-force search space
* Entropy in bits
* Strength rating
* Estimated brute-force crack time

For example, the program can analyze a password such as:

Hello123

and produce a report containing its characteristics and mathematical security estimates.

## Architecture

The project uses two primary classes.

### `Password`

Responsible for storing and analyzing the password itself.

It determines:

Password
 ├── length
 ├── uppercase count
 ├── lowercase count
 ├── digit count
 └── symbol count

### `PasswordAnalyzer`

Receives the Password object and performs the mathematical analysis.

Its responsibilities include:

PasswordAnalyzer
 ├── character pool
 ├── search space
 ├── entropy
 ├── strength rating
 ├── crack-time estimate
 └── formatted report

This separation allowed me to practice passing objects between classes and organizing responsibilities instead of placing the entire program into one large block of code.

---

## Mathematical Model

The estimated brute-force search space is based on:

search space = character pool ^ password length

The theoretical entropy is calculated using:

entropy = password length × log₂(character pool)

The current model assumes:

* 26 lowercase letters
* 26 uppercase letters
* 10 digits
* 32 symbols

Only character categories detected in the password contribute to the estimated character pool.

For the crack-time estimate, the program currently assumes:

1,000,000 guesses per second

The resulting value is then converted into a more readable unit such as seconds, minutes, hours, days, months, or years.

---

## Important Limitations

This project is an **educational mathematical model**, not a professional password-cracking or password-auditing tool.

The calculated values should not be interpreted as guarantees of real-world password security.

Real attacks can involve:

* Dictionary attacks
* Password leaks and breached-password databases
* Common password patterns
* Password reuse
* Hardware differences
* Different hashing algorithms
* Optimized cracking techniques
* Online versus offline attack environments

The project's character pool is also a simplified model based primarily on common ASCII character categories.

An important distinction is that **theoretical entropy is not necessarily the same as the true unpredictability of a human-created password**. A password can have a large theoretical search space while still being predictable because of the way it was constructed.

---

## Testing

The project includes automated tests using pytest.

The tests verify the expected behavior of the password analysis and mathematical calculations, including:

* Password characteristics
* Character pool
* Search space
* Entropy
* Strength rating
* Crack-time calculation

Tests can be run with:

pytest

The project also includes a requirements.txt file containing the external dependency required for testing.

---

## Repository Structure

CS50P/
│
├── Week 0/
├── Week 1/
├── Week 2/
├── Week 3/
├── Week 4/
├── Week 5/
├── Week 6/
├── Week 7/
├── Week 8/
├── Week 9/
│
└── Final Project/
    ├── project.py
    ├── test_project.py
    ├── requirements.txt
    └── README.md

The exact organization of the weekly directories may vary depending on the original CS50 problem-set structure.

---

## Development Philosophy

One of the biggest lessons I took from CS50P was that programming is not simply about knowing the syntax of a language.

A large part of the process is learning how to:

Understand the problem
        ↓
Break it into smaller problems
        ↓
Design a solution
        ↓
Implement it
        ↓
Run it
        ↓
Debug it
        ↓
Test it
        ↓
Improve it

There were plenty of moments throughout this course where concepts that initially seemed simple became surprisingly difficult once I actually had to implement them.

OOP was one of those areas.

The final project became an opportunity to put those concepts together in one program rather than treating them as isolated exercises.

---

## What This Repository Represents

This repository is primarily a record of my learning process.

It contains the progression from basic Python exercises to a complete project involving:

**Python → Object-Oriented Programming → Mathematics → Testing → Documentation → Project Design**

The code is not intended to represent the most sophisticated possible implementation of these ideas. Instead, it represents where my programming ability reached after completing CS50P and the process I went through to get there.

---

## Completion

**CS50P — Introduction to Programming with Python**

**Completed:** August 2026

This course gave me my first structured foundation in Python and programming, and it serves as a starting point for continuing into more advanced computer science topics.

### Next Step

**CS50x — Introduction to Computer Science**

The next goal is to take the foundation developed here and apply it to a broader range of computer science concepts, including algorithms, data structures, memory, databases, and web development.

---

### Certificate

I completed CS50P and received the official CS50 certificate for the course.

URL link:
https://certificates.cs50.io/3ca3c715-cacc-41ca-b80c-633fa30a8bf9.pdf?size=letter

---

> *From writing my first Python programs to designing and testing my own final project — CS50P was where I started taking programming seriously.*
