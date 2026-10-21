# Read the text from poems.txt and check if it contains the word twinkle.
with open("poems.txt", "r") as f:
    content = f.read()

if "twinkle" in content.lower():
    print("Yes, 'twinkle' is present.")
else:
    print("No, 'twinkle' not found.")


# Guess the number game
import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess > number:
        print("Lower number please")
    elif guess < number:
        print("Higher number please")
    else:
        print(f"You guessed it right in {attempts} attempts!")
        break



# Replace word Donkey with #######
with open("sample.txt", "r") as f:
    content = f.read()

content = content.replace("Donkey", "#######")

with open("sample.txt", "w") as f:
    f.write(content)



# Replace multiple words with #######
words_to_censor = ["Donkey", "Idiot", "Stupid"]

with open("sample.txt", "r") as f:
    content = f.read()

for word in words_to_censor:
    content = content.replace(word, "#######")

with open("sample.txt", "w") as f:
    f.write(content)



# Check if log file contains python
with open("log.txt", "r") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes, 'python' found in log file.")
else:
    print("No, 'python' not found.")



# Find line number where python is present
with open("log.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        if "python" in line.lower():
            print(f"'python' found at line {i}")



# Make a copy of this.txt
with open("this.txt", "r") as f:
    content = f.read()

with open("copy.txt", "w") as f:
    f.write(content)



# Check if two files are identical
def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        return f1.read() == f2.read()

print(compare_files("file1.txt", "file2.txt"))



# Wipe out contents of a file
with open("sample.txt", "w") as f:
    f.write("")   # clears file



# Rename a file
import os
os.rename("oldfile.txt", "renamed_by_python.txt")


















