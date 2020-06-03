import sys 

def FindHighestNum(peaks):
    highest = 0
    for entry in peaks:
        if int(entry) > highest:
            highest = int(entry)
    return highest
    #returns largest number

def RoutePlanner(peaks, highest):
    target = peaks.index(highest)
    current = 0
    journey = list()
    for i in range(0, target+1):
        for peak in peaks:
            if peak > current:
                current = peak 
                journey.append(current)
    return journey

def GetInput(args):
    input_list = list()
    for i in range(1, len(args)):
        input_list.append(int(args[i]))
    return input_list

try:
    #sys.argv[1] is the input
    peaks = GetInput(sys.argv)
    highest = FindHighestNum(peaks)
    print(highest)
    route = RoutePlanner(peaks, highest)
    for entry in route:
        print(entry, end =' ')
    print("\n")

except ValueError:
    print("Argument(s) missing")
except IndexError:
    print("Argument(s) missing")