import sys 

def FindHighestNum(peaks):
    highest = 0 
    for entry in peaks:
        if int(entry) > highest:
            highest = int(entry)
    return highest
    #returns largest number

def FindLowestPeak(peaks, Current, Highest):
    tmp_list = list()
    for i in range(Current-1, Highest+1):
        if peaks[i] > Current:
            print(peaks[i])
            tmp_list.append(peaks[i])
    return int(min(tmp_list))

def RoutePlanner(peaks, highest):
    target = peaks.index(highest)
    current = 0
    journey = list()
    for i in range(0, target+1):
        for peak in peaks:
            if peak > current:
                next_peak = FindLowestPeak(peaks, peaks.index(current), target)
                journey.append(next_peak)
    return journey

def GetInput(args):
    input_list = list()
    for i in range(1, len(args)):
        input_list.append(int(args[i]))
    return input_list

#sys.argv[1] is the input
peaks = GetInput(sys.argv)
highest = FindHighestNum(peaks)
route = RoutePlanner(peaks, highest)
for entry in route:
    print(entry, end =' ')
print("\n")
