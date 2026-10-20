# while loop
i = 0
while i<10:
    print("Yes " + str(i))
    i = i + 1

print("Done")


# quick quiz
i = 1

while i<=50:
    print(i)
    i = i + 1


# print list
fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1

# print list for
fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']

for item in fruits:
    print(item)
   
# range function
for i in range(1, 8, 1):
    print(i)


# for with else
for i in range(10):
    print(i)
else:
    print("This is inside else of for")


# break statement
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")

# continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)


# pass statement
i = 4

def run(player):
    pass

def ouch(player):
    pass

if i>0:
    pass

while i>6:
  pass

print("Harry is a good boy")




# Multiplication table using for loop
num = int(input("Enter the number"))
for i in range(1, 11):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")





# Greet names starting with 'S'
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)




# Multiplication table using while loop
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1




#  Prime number check
num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")




# Sum of first n natural numbers using while loop
n = int(input("Enter n: "))
i, total = 1, 0
while i <= n:
    total += i
    i += 1
print("Sum =", total)



# Factorial using for loop
# n! = 1 X 2 X 3 X ..... X n
# 5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")


#  Star pattern (n=3)
n = 3
for i in range(n):
    print("*" * (2*i+1))

#  Centered star pattern (n=3)
n = 3
for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i+1))

# Inverted star pattern (n=3)
n = 3
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))

#  Reverse multiplication table
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n*i}")
































