# app.py — second update

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# --- New Feature 2: Temperature Converter ---
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"212°F = {fahrenheit_to_celsius(212)}°C")