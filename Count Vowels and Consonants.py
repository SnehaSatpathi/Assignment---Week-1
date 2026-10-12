# Count Vowels and Consonants

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
v = sum(1 for ch in s if ch in vowels)
c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
print("Vowels:", v)
print("Consonants:", c)
