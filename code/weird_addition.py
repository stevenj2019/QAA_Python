def weirdmaths(input):
    input = str(input)
    d1 = input
    d2 = input+input
    d3 = input+input+input
    d4 = input+input+input+input
    return int(d1) + int(d2) + int(d3) + int(d4)