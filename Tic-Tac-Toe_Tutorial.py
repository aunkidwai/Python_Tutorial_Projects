print('Tic-Tac-Toe Console v1 ')

Turns = 9
Round = 0

print('\nPositions:')

matrix = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]

Game = {'00': '   ', '01': '   ', '02': '   ',
        '10': '   ', '11': '   ', '12': '   ',
        '20': '   ', '21': '   ', '22': '   '
        }

print()
for i in range(len(matrix)):  # range(3) (0,3)
    for j in range(len(matrix[i])):
        print(' ' + str(i) + str(j) + ' ', end='')  # 00 01 02
    print()
print()

xy = ''

while Turns > 0:
    if Turns % 2 == 0:
        sign = ' O '
        player = 2
    else:
        sign = ' X '
        player = 1

    Round += 1
    if Round == 9:
        print('Final Round')
    else:
        print('Round:', Round)

    print('Player:', player)
    xy = input("Enter position [Format: xy]: ")  # 01
    x, y = list(xy)

    if int(x) in [0, 1, 2] and int(y) in [0, 1, 2] and xy in Game.keys() and Game[xy] == '   ':
        print('Valid Input')
        Game[xy] = sign

        print()  # 01
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):  # 01
                if xy == (str(i) + str(j)):  # 01 = 01
                    print(sign, end='')
                else:
                    print(Game[(str(i) + str(j))], end='')
            print()
        print()
    else:
        Round -= 1
        print('\nInvalid Entry! Please Try Again\n')
        continue

    Turns -= 1

    if Game['00'] == Game['01'] == Game['02'] == ' X ' or Game['10'] == Game['11'] == Game['12'] == ' X ' or Game[
        '20'] == Game['21'] == Game['22'] == ' X ' or Game['00'] == Game['10'] == Game['20'] == ' X ' or Game['01'] == \
            Game['11'] == Game['21'] == ' X ' or Game['02'] == Game['12'] == Game['22'] == ' X ' or Game['00'] == Game[
        '11'] == Game['22'] == ' X ' or Game['02'] == Game['11'] == Game['20'] == ' X ':
        print('Player ' + str(player) + ' Won')
        break
    elif Game['00'] == Game['01'] == Game['02'] == ' O ' or Game['10'] == Game['11'] == Game['12'] == ' O ' or Game[
        '20'] == Game['21'] == Game['22'] == ' O ' or Game['00'] == Game['10'] == Game['20'] == ' O ' or Game['01'] == \
            Game['11'] == Game['21'] == ' O ' or Game['02'] == Game['12'] == Game['22'] == ' O ' or Game['00'] == Game[
        '11'] == Game['22'] == ' O ' or Game['02'] == Game['11'] == Game['20'] == ' O ':
        print('Player ' + str(player) + ' Won')
        break
else:
    print('Tie')
