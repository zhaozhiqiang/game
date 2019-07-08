import os
import random
import platform
from line import Line

MAX_INDEX_IN_LINE = 3

if 'Windows' == platform.system():
    CLEAR_COMMAND = 'cls'
else:
    CLEAR_COMMAND = 'clear'


class Table():

    def __init__(self, table):
        self.table_changed = False
        self.table = table

        self.lines = [
            Line(self.table[0]),
            Line(self.table[1]),
            Line(self.table[2]),
            Line(self.table[3])
        ]

    def show_table(self):
        os.system(CLEAR_COMMAND)
        for line in self.lines:
            line.show_line()

    def left(self):
        for line in self.lines:
            line.set_changed(False)
            line.left()
            if line.get_changed():
                self.set_table_changed(True)

        self.update_lines()

    def right(self):
        for line in self.lines:
            line.set_changed(False)
            line.right()
            if line.get_changed():
                self.set_table_changed(True)

        self.update_lines()

    def up(self):
        lines_vertical = self.get_lines_vertical()
        for line in lines_vertical:
            line.set_changed(False)
            line.left()
            if line.get_changed():
                self.set_table_changed(True)

        self.update_table(lines_vertical)
        self.update_lines()

    def down(self):
        lines_vertical = self.get_lines_vertical()
        for line in lines_vertical:
            line.set_changed(False)
            line.right()
            if line.get_changed():
                self.set_table_changed(True)

        self.update_table(lines_vertical)
        self.update_lines()

    def get_lines_vertical(self):
        table_vertical = [
            [self.table[0][0], self.table[1][0],
             self.table[2][0], self.table[3][0]],
            [self.table[0][1], self.table[1][1],
             self.table[2][1], self.table[3][1]],
            [self.table[0][2], self.table[1][2],
             self.table[2][2], self.table[3][2]],
            [self.table[0][3], self.table[1][3],
             self.table[2][3], self.table[3][3]]
        ]

        lines_vertical = [
            Line(table_vertical[0]),
            Line(table_vertical[1]),
            Line(table_vertical[2]),
            Line(table_vertical[3])
        ]

        return lines_vertical

    def lines_vertical_to_table_vertical(self, lines_vertical):
        table_vertical = []
        for line in lines_vertical:
            table_vertical.append(line.get_line())
        return table_vertical

    def update_table(self, lines_vertical):
        table_vertical = self.lines_vertical_to_table_vertical(lines_vertical)
        self.table = [
            [table_vertical[0][0], table_vertical[1][0],
             table_vertical[2][0], table_vertical[3][0]],
            [table_vertical[0][1], table_vertical[1][1],
             table_vertical[2][1], table_vertical[3][1]],
            [table_vertical[0][2], table_vertical[1][2],
             table_vertical[2][2], table_vertical[3][2]],
            [table_vertical[0][3], table_vertical[1][3],
             table_vertical[2][3], table_vertical[3][3]],
        ]

    def update_lines(self):
        self.lines = [
            Line(self.table[0]),
            Line(self.table[1]),
            Line(self.table[2]),
            Line(self.table[3])
        ]

    def get_table_changed(self):
        return self.table_changed

    def set_table_changed(self, changed):
        self.table_changed = changed

    def game_over(self, success):
        if True == success:
            print('game pass😄')
        else:
            print('game over😭')

        os.system('./clean.sh')
        exit()

    def find_equal(self, lines):
        for line in lines:
            if line.find_equal():
                return True

        return False

    def could_not_move(self):
        return not (self.find_equal(self.lines) or self.find_equal(self.get_lines_vertical()))

    def num_in_table(self, num):
        for line in self.table:
            if num in line:
                return True
        return False

    def check(self, max_num):
        if self.num_in_table(max_num):
            self.game_over(True)
        elif not self.num_in_table(0) \
                and self.could_not_move():
            self.game_over(False)

    def new_num(self):
        if not self.num_in_table(0):
            return

        row = random.randint(0, MAX_INDEX_IN_LINE)
        column = random.randint(0, MAX_INDEX_IN_LINE)

        if 0 == self.table[row][column]:
            self.table[row][column] = int(random.choice('24'))
        else:
            self.new_num()
