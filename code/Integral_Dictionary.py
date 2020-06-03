import sys

def IntegralDictionary(n):
    Integrals = {}
    for i in range(1, n+1):
        Integrals[i] = i*i
    return Integrals

try:
    output = IntegralDictionary(int(sys.argv[1]))
    for i in range(1, len(output)+1):
        print(str(i) +": "+ str(output[i])+"\t", end='')
    print("\n")
except IndexError:
    print("Parameter Required")