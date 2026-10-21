# oops
class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

# a = 12
# b = 34

# print("The sum of a and b is ", a+b)

'''
PascalCase 
EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''





# railway oops
import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"
harrysApplication.printData()




# game example
class Remote():
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()





# employee
class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400

print(harry.company)
print(rajni.company)
Employee.company = "YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)





# instance class attributes
 class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45
print(harry.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 





# self
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000
harry.getSalary() # Employee.getSalary(harry)




# static method
class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") # Employee.getSalary(harry)
harry.greet() # Employee.greet()
harry.time()




# constructor
class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee("Harry", 100, "YouTube")
# harry = Employee() --> This throws an error (missing 3 required positional arguments:)
harry.getDetails()




# Class Programmer for storing info of programmers at Microsoft
class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"Programmer {self.name} works on {self.product} at {self.company}.")

p1 = Programmer("Sneha", "Azure")
p2 = Programmer("Ravi", "Office")
p1.getInfo()
p2.getInfo()




# Class Calculator for square, cube, square root
import math

class Calculator:
    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

    def squareRoot(self, n):
        return math.sqrt(n)

calc = Calculator()
print(calc.square(4))
print(calc.cube(3))
print(calc.squareRoot(16))



# Class attribute vs object attribute
class Sample:
    a = 10

obj = Sample()
print("Before:", Sample.a, obj.a)

obj.a = 0   # changes only object attribute
print("After:", Sample.a, obj.a)
# This shows that setting obj.a does not change the class attribute.



# Add static method to greet user
class Calculator:
    @staticmethod
    def greet():
        print("Hello, welcome to Calculator!")

    def square(self, n):
        return n * n

Calculator.greet()



# Class Train with booking, status, fare
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Train {self.name} has {self.seats} seats available.")

    def getFareInfo(self):
        print(f"Ticket price for {self.name} is Rs {self.fare}.")

    def bookTicket(self):
        if self.seats > 0:
            print("Ticket booked successfully!")
            self.seats -= 1
        else:
            print("Sorry, no seats available.")

rajdhani = Train("Rajdhani Express", 1500, 2)
rajdhani.getStatus()
rajdhani.getFareInfo()
rajdhani.bookTicket()
rajdhani.getStatus()




# Change self parameter name
class Sample:
    def __init__(harry, value):   # using 'harry' instead of self
        harry.value = value

    def show(harry):
        print(f"Value is {harry.value}")

obj = Sample(10)
obj.show()

# Works fine! You can rename self to anything (slf, harry, etc.), but by convention we always use self.


































