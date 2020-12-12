# write your code here
def winner(temp_list, temp_mat):
    number_of_x = temp_list.count('X')
    number_of_o = temp_list.count('O')

    if abs(number_of_x - number_of_o) > 1:
        print('Impossible')
    else:
        win_x = 0
        win_o = 0
        for i in range(3):
            if "".join(temp_mat[i]) == 'XXX':
                win_x += 1
            if "".join(temp_mat[i]) == 'OOO':
                win_o += 1
            if temp_mat[0][i] == temp_mat[1][i] == temp_mat[2][i] == 'X':
                win_x += 1
            if temp_mat[0][i] == temp_mat[1][i] == temp_mat[2][i] == 'O':
                win_o += 1

        # For Diagonals:
        if temp_mat[0][0] == temp_mat[1][1] == temp_mat[2][2] == 'X':
            win_x += 1
        if temp_mat[0][0] == temp_mat[1][1] == temp_mat[2][2] == 'O':
            win_o += 1
        if temp_mat[0][2] == temp_mat[1][1] == temp_mat[2][0] == 'X':
            win_x += 1
        if temp_mat[0][2] == temp_mat[1][1] == temp_mat[2][0] == 'O':
            win_o += 1

        if win_x == win_o == 1:
            return 'Impossible'
        elif win_x == 1:
            return 'X wins'
        elif win_o == 1:
            return 'O wins'

        for i in range(3):
            for j in range(3):
                if temp_mat[i][j] == '_':
                    return 'Game not finished'
        return 'Draw'


def print_list(temp_list):
    temp_mat = []

    print('---------')
    k = 0
    for i in range(3):
        print('| ', end='')
        a = []
        for j in range(3):
            if temp_list[k] != '_':
                print(temp_list[k], end=' ')
            elif temp_list[k] == '_':
                print(" ", end=' ')
            a.append(temp_list[k])
            k = k + 1
        print('|')
        temp_mat.append(a)
    print('---------')
    return temp_mat


def analyze_coordinates(x, y, temp_mat):
    if not x.isdigit() or not y.isdigit():
        print("You should enter numbers!")
        return True
    x = int(x)
    y = int(y)
    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Coordinates should be from 1 to 3!")
        return True
    elif temp_mat[abs(y - 3)][abs(x - 1)] != '_':
        print("This cell is occupied! Choose another one!")
        return True
    return False


def mat_to_list(temp_mat):
    for i in range(3):
        temp_mat[i] = "".join(temp_mat[i])
    temp_list = "".join(temp_mat)
    return temp_list


# Main

input_list = ('_', '_', '_', '_', '_', '_', '_', '_', '_')
result = 'Game not finished'
symbol = 'X'
temp = 'O'
M = print_list(input_list)

while result == 'Game not finished':
    flag = True

    while flag:
        coordinate_x, coordinate_y = input("Enter the coordinates: > ").split()
        flag = analyze_coordinates(coordinate_x, coordinate_y, M)

    coordinate_x = int(coordinate_x)
    coordinate_y = int(coordinate_y)
    M[abs(coordinate_y - 3)][abs(coordinate_x - 1)] = symbol

    symbol, temp = temp, symbol

    input_list = mat_to_list(M)

    M = print_list(input_list)
    result = winner(input_list, M)

print(result)