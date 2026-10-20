# function
def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
    return p

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)
print(percentage1, percentage2)



# quick quiz
def greet(name):
    print("Good Day, "+ name)

def mySum(num1, num2):
    return num1 + num2

greet("Harry")
s = mySum(6, 32)
print(s)



# default arguments
def greet(name="Stranger"):
    print("Good Day, "+ name)
 

greet("Harry") 
greet()



# factorial
# n! = 1 * 2 * 3 * 4...*n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)! 

# n = 0
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

# f = factorial_iter(5)
f = factorial_recursive(0)
print(f)




# Greatest of three numbers
def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(13, 55, 2)
print("The value of the maximum is " + str(m))



# Celsius to Fahrenheit
def farh(cel):
    return (cel *(9/5)) + 32
c = 0
f = farh(c)
print("Fahreheit Temperature is " + str(f))


# Prevent newline in print()
print("Hello", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?", end=" ")




# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n
# Recursive sum of first n natural numbers
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)

print("Sum:", recursive_sum(5))



# Pattern printing
n = 3
for i in range(n):
    print("*" * (n-i)) # Prints * n-i times



# Inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54

print("Centimeters:", inches_to_cm(10))




# Remove word from list and strip
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Harry is a good      "
n = remove_and_split(this, "Harry")
print(n)
# print(this)
# print(this.strip())



#  Multiplication table
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

table(7)






























