# Student Grade Calculator : Take marks as input, calculate average & assign grades.

def grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        g = "A"
    elif avg >= 80:
        g = "B"
    elif avg >= 70:
        g = "C"
    elif avg >= 60:
        g = "D"
    else:
        g = "F"
    return avg, g

n = int(input("Enter number of subjects: "))
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(n)]

avg, g = grade(marks)
print("Average:", avg)
print("Grade:", g)

