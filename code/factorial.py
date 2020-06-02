import sys
#input uses sys.argv[1]

def factorial(Input):
    factorial = 1
    for num in range(1, int(Input)+1):
        factorial = factorial * num
    return factorial

try:
    if int(sys.argv[1]) >= 1:
        print(factorial(sys.argv[1]))
    else:
        print("Invalid input")
except IndexError:
    print("arg not provided")    