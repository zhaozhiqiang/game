#!/usr/bin/env python3

from table import Table
from pynput.keyboard import Key, Listener
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='2048.log',
                    filemode='w',
                    format='%(message)s')

MAX_NUM = 2048
t = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
table = Table(t)

def on_press(key):
    if Key.up == key:
        logging.debug('\n上')
        table.up()
    elif Key.down == key:
        logging.debug('\n下')
        table.down()
    elif Key.left == key:
        logging.debug('\n左')
        table.left()
    elif Key.right == key:
        logging.debug('\n右')
        table.right()
    else:
        table.game_over(False)

    # 表格有变动则增加数字
    if table.get_table_changed():
        table.new_num()
        table.set_table_changed(False)

    table.show_table()
    table.check(MAX_NUM)


table.new_num()
table.new_num()
table.show_table()


with Listener(on_press=on_press) as listener:
    listener.join()
