import art


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
    }

print(art.logo)

restart = True
q = ""

result = 0.0

while restart:

    if q == 'y':
        num1 = result
    else:
        num1 = float(input("What is the first number?: "))

    for symbols in operations:
        print(symbols)

    op = str(input("Pick an operation: "))

    num2 = float(input("What is the second number?: "))

    result = operations[op](num1, num2)
    print(f"{num1} {op} {num2} = {result}")

    q = input("Type 'y' to continue calculating with #result, or type 'n' to start a new calculation or type 'q' to quit: ")

    if q == "q":
        restart = False
        print("Thank you for using PyCalculator!")
    elif q == "n":
        restart = True
        result = 0.0
        print("\n" * 20)  # scroll down to new screen
        print(art.logo)
    elif q == "y":
        restart = True