# Dictionary Syntax


myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'}
}

# print(myDict['Fast'])
# print(myDict['Harry'])
myDict['Marks'] = [45, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['harry'])




# Dictionary Methods
myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "harry": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harry")) # Prints value associated with key "harry"
print(myDict["harry"]) # Prints value associated with key "harry"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
print(myDict["harry2"]) # throws an error as harry2 is not present in the dictionary





# Sets
a = {1, 3, 4, 5, 1}
print(type(a))
print(a)



# empty sets
# Important: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))
# An empty set can be created using the below syntax:
b = set()
print(type(b))



# set methods
# Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())
print(b)



# Create a dictionary of Hindi words with values as their English translation. Provide the user an option to look it up.
myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))




# Input eight numbers from the user and display all the unique numbers (once)
num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)




# Input numbers from the user and store them in a set.
s = {18, "18", 18.1}
print(s)




s = {20, 20.0, "20"}
print(s)
print(len(s))  # 3


s = set()
print(type(s)) # <class 'set'>


# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume names are unique.
favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)



# If names of 2 friends are same, what will the program in Problem 5 do?
# The later entry will overwrite the earlier one because dictionary keys must be unique.













































