# virtual environment
# For MacOS/linux users: source myprojectenv/bin/activate
# For windows powershell users: .\myprojectenv\Scripts\activate.ps1
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

import flask # flask - 0.5.2
import pandas as pd
import pygame



# lambda
# def func(a):
#     return a+5

func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6



# join
l = ["Camera", "Laptop", "Phone", "ipad", "Hard Disk", "Nvidia Graphic 3080 card"]

# sentence = "~~".join(l)
# sentence = "==".join(l)
sentence = "\n".join(l)
print(sentence)
print(type(sentence))



# format
name = "Harry"
channel = "CodeWithHarry"
type = "Coding"
# a = f"This is {name}"
# a = "This is {}".format(name)
# a = "This is {} and his channel is {}".format(name, channel)
# a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
a = "This is {} and his {} channel is {}".format(name, channel, type)

print(a)



# map
def square(num):
    return num*num

l = [1, 2, 4]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# Method 2
print(list(map(square, l)))



# filter
# Filter Syntax: list(filter(function, list))
def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

g10 = lambda num: num>10

l = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]
print(list(filter(greater_than_5, l)))
print(list(filter(g10, l)))


# reduce
from functools import reduce

sum = lambda a, b: a+b

l = [1, 2, 3, 4]
val = reduce(sum, l)
print(val)




#  Q1: Create two virtual environments and replicate packages
python -m venv env1
source env1/bin/activate   # Linux/Mac
env1\Scripts\activate      # Windows
pip install flask numpy pandas

# Export installed packages:
pip freeze > requirements.txt

# Second environment:
python -m venv env2
source env2/bin/activate
pip install -r requirements.txt

# This way, both environments have the same packages.



# Format student details using format()
name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter your phone number: ")

template = "The name of the student is {}, his marks are {} and phone number is {}"
output = template.format(name, marks, phone)
print(output)



# Convert multiplication table of 7 into vertical string
table = [7 * i for i in range(1, 11)]
vertical_string = "\n".join(map(str, table))
print(vertical_string)


# Filter numbers divisible by 5
numbers = [10, 23, 45, 67, 90, 12, 25]
divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(divisible_by_5)


# Find maximum using reduce
from functools import reduce

numbers = [10, 23, 45, 67, 90, 12, 25]
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum number is:", max_num)


# Replicate environment using pip freeze
pip freeze > requirements.txt
pip install -r requirements.txt


# Create a Flask web server
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Sneha! Welcome to Flask server."

if __name__ == "__main__":
    app.run(debug=True)

































