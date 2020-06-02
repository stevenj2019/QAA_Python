import sys 

def ISBN(numbers):
    check_sum=0
    for number in numbers:
        if int(number) % 2 == 0:
            temp = int(number) * 3
            check_sum = check_sum + temp 
        else:
            check_sum = check_sum + int(number)
    return check_sum
try: 
    inp = list(''.join(sys.argv[1].split("-")))
    if len(inp) == 12:
        check_sum = 10 - ISBN(list(inp)) % 10
        print(check_sum)
    else:
        print("Number too long/short")
except IndexError:
    print("Argument Missing")