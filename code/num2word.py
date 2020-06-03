import sys
from collections import deque

def _numSplitter(number):
    array = list()
    number = list(number)
    size = len(number)
    while size != 0:
        if size >= 3:
            temp = [number[len(number)-3], number[len(number)-2], number[len(number)-1]]
            array.append(temp)
            del number[len(number)-1]
            del number[len(number)-1]
            del number[len(number)-1]
        elif size >= 2:
            temp = [number[len(number)-1], number[len(number)-2]]
            array.append(temp)
            del number[len(number)-1]
            del number[len(number)-1]
        elif size >= 1:
            array.append(number[0])
            del number[len(number)-1]
        else:
            print("error has occured")
            break
        
        size = len(number)

    return array

def _dequeConv(deque_list):
    output = list()
    for i in deque_list:
        output.append(i)
    return output

def _numberCompiler(number):
    tmp_str = list()
    if number[0] != 0:
        tmp_str.append(num2words[int(number[0])] + " hundred")

    num = int(number[1] + number[2])
    if num in num2words.keys():
        tmp_str.append(num2words[num])
    else:
        tmp_str.append(num2words[int(number[1]+"0")])
        tmp_str.append(num2words[int(number[2])])
    return tmp_str

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

units = ["Thousand", "Million", "Billion", "Trillion"]

number = _numSplitter(sys.argv[1]) #3d array
counter = 0
output = deque()
tmp_str = list()
size = len(number)
while counter != size:
    if counter == 0:
        print(counter)
        output.append(_numberCompiler(number[0]))
        del number[0]
    else:
        tmp_str = _numberCompiler(number[0])
        print(tmp_str)
        tmp_str.append(units[counter])
    
    print(tmp_str)
    output.appendleft(tmp_str)
    counter = counter + 1

output = _dequeConv(output)
for sub in output:
    for string in sub:
        print(string, end=' ')
print("\n")