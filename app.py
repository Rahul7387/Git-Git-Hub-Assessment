# app.py — updated with new features

def greet(name):
    return f"Hello, {name}!"

# --- New Feature 1: Calculator ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")