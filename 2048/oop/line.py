import logging


RIGHT = -1
LEFT = 1
CELL_WIDTH = 5
MAX_INDEX_IN_LINE = 3


class Line():

    def __init__(self, line):
        self.line = line
        self.changed = False

    def get_line(self):
        return self.line

    def show_line(self):
        shown_line = self.line_to_string()

        print(shown_line + '\n')
        logging.debug('\n' + shown_line)

    def line_to_string(self):
        shown_line = ''
        for num in self.line:
            if 0 == num:
                shown_line += '·' + ' ' * (CELL_WIDTH - 1)
            else:
                shown_line += (str(num) + ' ' * (CELL_WIDTH - len(str(num))))
        return shown_line

    def reverse(self):
        self.line.reverse()

    def left(self):
        self.plus()
        self.move()

    def right(self):
        self.reverse()
        self.plus()
        self.move()
        self.reverse()

    def next_not_zero(self, index):
        index += 1
        while index <= 3:
            if 0 != self.line[index]:
                return index
            else:
                index += 1
        return -1

    def get_changed(self):
        return self.changed

    def set_changed(self, changed):
        self.changed = changed

    def plus(self):
        i = 0
        while i <= 3:
            if 0 != self.line[i]:
                j = self.next_not_zero(i)
                if -1 != j \
                        and self.line[i] == self.line[j]:
                    self.line[i] += self.line[j]
                    self.line[j] = 0
                    self.set_changed(True)
            i += 1

        return self.line

    def move(self):
        i = 0
        while i <= 3:
            if 0 == self.line[i]:
                j = self.next_not_zero(i)
                if -1 != j:
                    self.line[i] = self.line[j]
                    self.line[j] = 0
                    self.set_changed(True)
            i += 1

        return self.line

    def full(self):
        if 0 in self.line:
            return False

        return True

    def find_equal(self):
        i = 0
        while i < MAX_INDEX_IN_LINE:
            if self.line[i] == self.line[i + 1]:
                return True
            i += 1
        return False