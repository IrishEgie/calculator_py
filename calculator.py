import art


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


print(art.logo)

restart = True
q = ""

result = 0.0

while restart:

    if q == 'y':
        num1 = result
    else:
        num1 = float(input("What is the first number?: "))

    for i in range (4):
        op_sym = ["+","-","*","/"]
        print(op_sym[i])

    op = str(input("Pick an operation: "))

    num2 = float(input("What is the second number?: "))


    if op == "*":
        result = mul(num1,num2)
        print(result)
    elif op=="/":
        result = div(num1,num2)
        print(result)
    elif op=="+":
        result = add(num1,num2)
        print(result)
    elif op=="-":
        result = sub(num1,num2)
        print(result)

    q = input("Type 'y' to continue calculating with #result, or type 'n' to start a new calculation or type 'q' to quit: ")

    if q=="q":
        restart=False
        print("Thank you for using PyCalculator!")
    elif q=="n":
        restart=True
        result=0.0
        print("\n"*20) #scroll down to new screen
        print(art.logo)
    elif q=="y":
        restart = True