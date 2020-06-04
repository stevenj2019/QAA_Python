import sys 

def Vowles(word):
    chars = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0 
    for letter in list(word):
        if chars.__contains__(letter.lower()):
            count = count + 1
    return count 

try: 
    print(Vowles(sys.argv[1]))
except IndexError:
    print("an arg must be provided")