import os
import random
import logging

GOAL = 2048
MAX_INDEX_IN_LINE = 3
CELL_WIDTH = 5
table_changed = False
table_horizontal = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


logging.basicConfig(level=logging.DEBUG,
                    filename='2048.log',
                    filemode='w',
                    format='%(message)s')


def get_table_changed():
    return table_changed


def set_table_changed(changed):
    global table_changed
    table_changed = changed


def game_over(success):
    if True == success:
        print('game pass😄')
    else:
        print('game over😭')

    os.system('./clean.sh')
    exit()


def full():
    for line in table_horizontal:
        if 0 in line:
            return False

    return True


def find_equal(table):
    for line in table:
        i = 0
        while 0 <= i < MAX_INDEX_IN_LINE:
            if line[i] == line[i + 1]:
                return True
            i += 1

    return False


def could_move():
    table_vertical = get_table_vertical()
    return find_equal(table_horizontal) or find_equal(table_vertical)


def check():
    if not full():
        for line in table_horizontal:
            for num in line:
                if GOAL == num:
                    game_over(True)
    else:
        if not could_move():
            game_over(False)


def new_num():
    if full():
        return

    line_index = random.randint(0, MAX_INDEX_IN_LINE)
    column_index = random.randint(0, MAX_INDEX_IN_LINE)

    if 0 == table_horizontal[line_index][column_index]:
        table_horizontal[line_index][column_index] = int(random.choice('24'))
    else:
        new_num()


def show_line(line):
    shown_line = ''
    for num in line:
        if 0 == num:
            shown_line += '·' + ' ' * (CELL_WIDTH - 1)
        else:
            shown_line += (str(num) + ' ' * (CELL_WIDTH - len(str(num))))
    print(shown_line)
    print('\n')

    logging.debug('\n' + shown_line)


def show_table():
    os.system('clear')
    # os.system('cls')
    for line in table_horizontal:
        show_line(line)


def move(line, step):
    i = 0 if -1 != step else MAX_INDEX_IN_LINE
    while 0 <= i <= MAX_INDEX_IN_LINE:
        if (0 == line[i]):
            j = next_not_zero(line, i, step)
            if -1 != j:
                line[i] = line[j]
                line[j] = 0
                set_table_changed(True)
        i += step

    return line


def next_not_zero(line, index, step):
    while 0 <= index and index <= MAX_INDEX_IN_LINE:
        if index + step < 0 or index + step > MAX_INDEX_IN_LINE:
            return -1
        elif 0 != line[index + step]:
            return index + step
        else:
            index += step
    return -1


def plus(line, step):
    '''
    step值代表数值合并的方向:
    1: 向左合并: [2, 2, 2, 2] -> [4, 0, 2, 2]
    -1: 向右合并: [2, 2, 2, 2] -> [2, 2, 0, 4]
    '''
    i = 0
    if -1 == step:
        i = MAX_INDEX_IN_LINE

    while 0 <= i and i <= MAX_INDEX_IN_LINE:
        if 0 != line[i]:
            j = next_not_zero(line, i, step)
            if (-1 != j) \
                    and (line[i] == line[j]):
                line[i] += line[j]
                line[j] = 0
                set_table_changed(True)
        i += step

    return line


def horizontal(step):
    # 1: move to left
    # -1: move to right
    for line in table_horizontal:
        line = plus(line, step)
        line = move(line, step)


def get_table_vertical():
    table_vertical = [
        [table_horizontal[0][0], table_horizontal[1][0],
            table_horizontal[2][0], table_horizontal[3][0]],
        [table_horizontal[0][1], table_horizontal[1][1],
            table_horizontal[2][1], table_horizontal[3][1]],
        [table_horizontal[0][2], table_horizontal[1][2],
            table_horizontal[2][2], table_horizontal[3][2]],
        [table_horizontal[0][3], table_horizontal[1][3],
            table_horizontal[2][3], table_horizontal[3][3]],
    ]

    return table_vertical


def vertical_to_horizontal(table_vertical):
    global table_horizontal
    table_horizontal = [
        [table_vertical[0][0], table_vertical[1][0],
            table_vertical[2][0], table_vertical[3][0]],
        [table_vertical[0][1], table_vertical[1][1],
            table_vertical[2][1], table_vertical[3][1]],
        [table_vertical[0][2], table_vertical[1][2],
            table_vertical[2][2], table_vertical[3][2]],
        [table_vertical[0][3], table_vertical[1][3],
            table_vertical[2][3], table_vertical[3][3]],
    ]


def vertical(step):
    # 1: move to left
    # -1: move to right
    table_vertical = get_table_vertical()
    for line in table_vertical:
        line = plus(line, step)
        line = move(line, step)

    vertical_to_horizontal(table_vertical)
