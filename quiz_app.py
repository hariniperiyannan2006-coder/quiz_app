# Simple Quiz Application
score = 0
print("Python Quiz")
answer = input("1. What is the extension of Python files? ")
if answer.lower() == ".py":
    score += 1
answer = input("2. Which keyword is used to define a function? ")
if answer.lower() == "def":
    score += 1
answer = input("3. Python is interpreted or compiled? ")
if answer.lower() == "interpreted":
    score += 1
answer = input("4. Which symbol is used for comments? ")
if answer == "#":
    score += 1
answer = input("5. Which data type stores True or False? ")
if answer.lower() == "boolean":
    score += 1
print("Your score is:", score, "/5")
