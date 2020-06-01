import sys
from collections import deque

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

units = ["Thousand", "Million", "Billion", "Trillion"]

#example number 4,988,364,712 == [[7, 1, 2], [3, 6, 4], [9, 8, 8], [4]]

try:
    number = _numSplitter(sys.argv[1])
    counter == 0
    output = deque()
    while counter <= len(number):
        if counter == 0:
            counter = counter + 1
            tmp_str = list()
            tmp_num = number[0].split("")
            if tmp_num[0] != 0:
                tmp_str.append(tmp_num[0] + " hundred")

            num = int(tmp_num[1] + tmp_num[2])
            if num2words[num].__exists__() == True:
                tmp_str.append(num2words[num])
            else:
                tmp_str.append(num2words[int(tmp_num[1])])
                tmp_str.append(num2words[int(tmp_num[2])])
                
            del number[0]
            counter = counter + 1
        else:
            tmp_num = number[0]
            tmp_str = []
            if tmp_num[0] != 0:
                tmp_str.append(tmp_num[0] + " hundred")
            
            num = int(tmp_num[1] + tmp_num[2])
            if num2words[num].__exists__() == True:
                tmp_str.append(num2wordsp[num + units[counter]])
            else:
                tmp_str.append(num2words[int(tmp_num[1])])
                tmp_str.append(num2words[int(tmp_num[1])])
                tmp_str.append(units[counter])

        output.appendleft(tmp_str)
    
    print(output.join(" "))

except IndexError:
    print("Parameter required")
    sys.exit()

def _numSplitter(number):
    array = list()
    number = number.split("")
    size = len(number)
    while size > 3:
        if size == 3:
            temp = [number[len(number)-1], number[len(number)-2], number[len(number)-3]]
            array.append(temp)
            del number[:-3]
        elif size == 2:
            temp = [number[len(number)-2], number[len(number)-2]]
            array.append(temp)
        elif size == 1:
            array.append(number[0])
        else:
            print("error has occured")

    return array