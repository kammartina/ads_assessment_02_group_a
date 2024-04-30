"""
Simple Calculator
"""
# Provide your solution here
def calculate(x: int, y: int, z: str):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        if x == 0 or y == 0:
            print("Division by 0 is not allowed.")
        else:
            return x / y
    else:
        print("Invalid operator.")
calculate(3,4,'+')

"""
Reverse Word
"""
# Provide your solution here
def reverse_word(word):
    i = -1
    length = len(word)
    for i in range(-1, -length - 1, -1):
        print(word[i])
    capitalized = word.capitalize()

reverse_word('martina')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")
