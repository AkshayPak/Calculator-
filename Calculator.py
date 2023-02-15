import math
def BasicCal(operation,v1,v2):
    match operation:
        case "+":
            print(v1+v2)
        case "-":
            print(v1-v2)
        case "*":
            print(v1*v2)
        case "/":
            print(v1/v2)
        case "%":
            print(v1%v2)
        case "**":
            print(v1**v2)
        case _:
            print("Invalid operator")

def SciCal(op,val):
    match op:
        case "log":
            print(math.log(val))
        case "sin":
            print(math.sin(val))
        case "cos":
            print(math.cos(val))
        case "tan":
            print(math.tan(val))
        case _:
            print("Invalid operator")



print('''Welcome
          1: For basic operations like +,-,/,*,**,%
          2: For scientific operations like sin log tan and cos''')
x = int(input())
if x == 1:
    o = input('''Enter the operation symbol for the operation to be performed
                 + : for addition
                 - : for subtraction
                 * : for multiplication
                 / : for division
                 % : for modulus
                 ** : for exponential''')
    y = int(input("Enter the first number:"))
    z = int(input("Enter the second number"))
    BasicCal(o,y,z)
elif x == 2:
    o = input('''Enter the operation to be performed
                 log : for Logarithmic operation
                 sin : to find the sine of the number
                 cos : to find the cos of the number
                 tan : to find the tan of the number''')
    y = int(input("Enter the number"))
    SciCal(o,y)
else:
    print("Invalid option")