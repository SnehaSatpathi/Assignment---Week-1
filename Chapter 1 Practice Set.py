import os  # importing the os module
print("Hello World")


#  Write a program to print Twinkle Twinkle Little Star poem in python
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')



# Install an external module and use it to perform an operation of your interest.
from playsound import playsound
playsound('D:\\MyData\\Business\\code playground\\Python Course With Notes\\1. Chapter 1\\play.mp3')



# Write a Python program to print the contents of a directory using os module.
import os
print(os.listdir())



# Use REPL and print the table of 5 using it.
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")



# Label the program written in Problem 4 with comments.
import os  # Importing the OS module
# os.listdir() returns a list of files/folders in the current directory
contents = os.listdir()
# Printing the contents
print("Files and folders in current directory:")
print(contents)












