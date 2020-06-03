def Maze_Printer(Maze):
    for line in Maze:
        for block in line:
            print(block, end='')
        print('\n')

#print('\n'.join('\t'.join('{:2}'.format(item) for item in row)for row in board))

#def GoStraight()
def Maze_Turner(Maze):
    Maze_Printer(Maze)


Maze_Turner([['#', '#', '#', '#', '#', '#', '#'],['#', '>', ' ', ' ', ' ', 'E', '#'],['#', '#', '#', '#', '#', '#', '#']])