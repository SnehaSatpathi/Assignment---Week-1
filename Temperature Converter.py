# Temperature Converter : Convert Celsius ↔ Fahrenheit using functions.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
c = 37
f = 98.6
print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")






