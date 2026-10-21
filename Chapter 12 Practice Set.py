# try
while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")


# handling different exceptions
try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
    
except ValueError as e:
    print("Please Enter a valid value") 

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0") 

print("Thanks for using this code!")


# raising exceptions
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry")

a = increment('df364')
print(a)


# try with else
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We were successful")


# try except finally
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")

print("Thanks for using the program")


# global
a = 54 # Global variable
def func1():
    global a
    print(f"Print statement 1: {a}")
    a = 8 # Local Variable if global keyword is not used
    print(f"Print statement 2: {a}")

func1()
print(f"Print statement 3: {a}")






def greet(name):
    print(f"Good morning, {name}")

# print(__name__)
if __name__ == "__main__":
    n = input("Enter a name\n")
    greet(n)



import m06_file1
m06_file1.greet("Harry")




list1 = [3, 53, 2, False, 6.2, "Harry"]

# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

for index, item in enumerate(list1):
    print(item, index)




a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# Shortcut to write the same:
b = [i for i in a if i%2==0]
print(b)

t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}
print(s)



def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")
        
readFile("1.txt")
readFile("2.txt")
readFile("3.txt")



l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(l):
    if index==2 or index== 4 or index==6:
        # print(index, item)
        print(f"The {index + 1}th element is {item}")



num = int(input("Enter your number: "))
table = [num*i for i in range(1, 11)]
print(table)



a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
try:
    print(a/b)
except:
    print("Infinite")




num = int(input("Enter your number: "))
table = [num*i for i in range(1, 11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table))
    f.write('\n')
























# Open three files 1.txt, 2.txt, 3.txt and handle missing files
files = ["1.txt", "2.txt", "3.txt"]

for filename in files:
    try:
        with open(filename, "r") as f:
            print(f"Contents of {filename}:")
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} not found!")


# Print 3rd, 5th, 7th element using enumerate
my_list = [10, 20, 30, 40, 50, 60, 70, 80]

for index, value in enumerate(my_list, start=1):
    if index in [3, 5, 7]:
        print(f"Element at position {index} is {value}")


# List comprehension for multiplication table
num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]
print(table)


# Handle division by zero
a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    print("Result:", a / b)
except ZeroDivisionError:
    print("Infinite")


# Store multiplication table in Tables.txt
num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]

with open("Tables.txt", "w") as f:
    f.write("\n".join([str(x) for x in table]))

print("Multiplication table saved to Tables.txt")








