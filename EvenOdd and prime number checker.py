# Even/Odd & Prime Number Checker

def check_even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
check_even_odd(num)

if is_prime(num):
    print(num, "is Prime")
else:
    print(num, "is Not Prime")


