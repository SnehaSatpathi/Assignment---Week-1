# Write a program to store seven fruits in a list entered by the user
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1} : ")
    fruits.append(fruit)
print("\n List of fruits entered: ")
print(fruits)


# write a program to accept marks of 6 students and display them in a sorted manner

marks = []
for i in range(6):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)
marks.sort()
print("\nSorted marks:", marks)


# check that a tuple cannot be changed in python
t = (1, 2, 3, 4)
print("Original tuple:", t)
try:
    t[0] = 99
except TypeError as e:
    print("Error:", e)


# write a program to sum a list with four numbers
numbers = [10, 20, 30, 40]
total = sum(numbers)
print("List:", numbers)
print("Sum of numbers:", total)


# write a program to count the number of zeros in the following tuple: a =(7,0,8,0,0,9)
a = (7, 0, 8, 0, 0, 9)
count_zeros = a.count(0)
print("Tuple:", a)
print("Number of zeros:", count_zeros)













