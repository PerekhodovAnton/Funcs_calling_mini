def add_two_numbers(a, b):
    return int(a) + int(b)

def subtract_two_numbers(a, b):
    return int(a) - int(b)

def multiply_two_numbers(a, b):
    return int(a) * int(b)

def divide_two_numbers(a, b):
    a = float(a)
    b = float(b)
    if b == 0:
        return "Error: Division by zero"
    return a / b

def total(nums):
    return sum(map(int, nums))


available_functions = {
    'add_two_numbers': add_two_numbers,
    'subtract_two_numbers': subtract_two_numbers,
    'multiply_two_numbers': multiply_two_numbers,
    'divide_two_numbers': divide_two_numbers,
    'total': total,
}