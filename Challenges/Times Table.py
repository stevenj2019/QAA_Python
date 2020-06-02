x_list = ['x', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
board = [x_list, ]
for num1 in range(1, 13):
    tmp_list = [int(num1), ]
    for num2 in range(1, 13):
        tmp_list.append(int(num1)*int(num2))
    board.append(tmp_list)
print('\n'.join('\t'.join('{:2}'.format(item) for item in row)for row in board))