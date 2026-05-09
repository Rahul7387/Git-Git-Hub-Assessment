# app.py — updated on feature-update branch

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# --- New Feature: String Utilities ---
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def word_count(s):
    return len(s.split())

# --- New Feature: List Utilities (WIP) ---
def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def calculate_average(lst):
    return sum(lst) / len(lst)

if __name__ == "__main__":
    print(greet("World"))
    print(f"Reverse of 'Python': {reverse_string('Python')}")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Word count of 'Hello World': {word_count('Hello World')}")
