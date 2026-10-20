# conditionals

a = 8

# 1. if-elif-else ladder in Python
# if(a<3): 
#     print("The value of a is greater than 3")
# elif(a>13):
#     print("The value of a is greater than 13")
# elif(a>7):
#     print("The value of a is greater than 7")
# elif(a>17):
#     print("The value of a is greater than 17")
# else:
#     print("The value is not greater than 3 or 7")

# 2. Multiple if statements
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("Done")


# if else quick quiz
age = int(input("Enter your age: "))

if age>18:
    print("Yes")
else:
    print("No")


# logical and relational operators
age = int(input("Enter your age: "))
if(age>34 or age<56):
    print("You can work with us")

else:
    print("You cannot work with us")



# in and is
# a = None
# if (a is None):
#     print("Yes")
# else:
#     print("No")

a = [45, 56, 6]
print(435 in a)



# is else optional
a = 6
if(a==7):
    print("yes")
elif(a>56):
    print("no and yes")
else:
    print("I am optional")



# werite a program to find greatest of four numbers entered by the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")




# write a program to find out whether a student is pass or fail if it requires total 40% and atleast 33% in each subject to pass. Assume  3 subjects and take marks as an input from the user
sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam")


# A spam comment is defined as a text containingfollowing keywords: "make a lot of money", "buy now","click this". write a program to detect these spams
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")



# write a program to find out whether a given post is talking about "Harry" or not
names = ["harry", "shubham", "rohit", "rohan", "aditi", "shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")



# write a program to calculate the grade of a student from his marks
marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)


# write a program to find whether a given username contain less than 10 characters or not

username = input("Enter your username: ")

# Check if the length of the username is less than 10
if len(username) < 10:
    print("The username contains less than 10 characters.")
else:
    print("The username contains 10 or more characters.")




# write a program which finds out whether a given name is present in a list or not

names_list = ["Alice", "Bob", "Charlie", "David", "Emma"]

# Get the name input from the user
search_name = input("Enter a name to search for: ")

# Check if the name is in the list (case-insensitive check)
if search_name.strip().title() in names_list:
    print(f"Yes, '{search_name}' is present in the list.")
else:
    print(f"No, '{search_name}' is not present in the list.")





























