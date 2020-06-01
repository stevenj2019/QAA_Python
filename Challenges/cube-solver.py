
cube = input(str("*********/*********/*********/*********/*********/*********"))

cube = _get3DList(cube)

def _get3DList(cube):
    sides = cube.split("/")
    new_list=list()
    for side in sides:
        temp = side.split("")
        new_list.append(temp)
    
    return new_list

def _getDaisy(cube):
    sides=cube.split("/"):
    #could be at position 2,4,6,8 on any side 
    counter = 1
    for side in sides:
        side+counter = side.split("")
        counter = counter + 1

def _getWhiteCross(cube):

def _getColourT(cube):