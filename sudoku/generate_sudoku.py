#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 30/09/2018 10:43 AM
@Author  : Jian
@Contact : l33klin@foxmail.com
@Site    : 
@File    : generate_sudoku.py
"""
import random

cells = [[0 for _ in range(9)] for __ in range(9)]
processed = [[False for _ in range(9)] for ___ in range(9)]
aval_lists = [[[] for _ in range(9)] for ____ in range(9)]


def get_valid_list(x, y):

    global cells

    la = set()

    for _ in range(9):
        la.add(cells[x][_])
        la.add(cells[_][y])

    x_s = int(x/3)
    y_s = int(y/3)

    for _x in [x_s*3 + i for i in range(3)]:
        for _y in [y_s*3 + i for i in range(3)]:
            la.add(cells[_x][_y])

    rl = [i+1 for i in range(9)]
    for i in la:
        if i in rl:
            rl.pop(rl.index(i))

    return rl


# cells[0] = [8, 4, 9, 7, 6, 0, 0, 0, 0]
# # cells[3][6] = 5
# print(get_valid_list(0, 5))


def get_next_coord(x, y):

    if y+1 < 9:
        return x, y+1
    elif x+1 < 9:
        return x+1, 0
    else:
        return 0, 0


def get_prev_coord(x, y):

    if y-1 >= 0:
        return x, y-1
    elif x-1 >= 0:
        return x-1, 8
    else:
        return 0, 0


def main():
    current_x = 0
    current_y = 0

    while True:
        global processed
        global aval_lists
        global cells
        if not processed[current_x][current_y]:

            aval_lists[current_x][current_y] = get_valid_list(current_x, current_y)
            # print("x:{}, y:{}\n{}".format(current_x, current_y, aval_lists[current_x][current_y]))
            processed[current_x][current_y] = True

        if aval_lists[current_x][current_y]:
            index = random.randint(0, len(aval_lists[current_x][current_y]) - 1)
            # value = aval_lists[current_x][current_y][index]
            value = aval_lists[current_x][current_y].pop(index)

            cells[current_x][current_y] = value
            current_x, current_y = get_next_coord(current_x, current_y)
            if current_x == 0 and current_y == 0:
                break

        elif current_x == 0 and current_y == 0:
            break
        else:
            processed[current_x][current_y] = False
            cells[current_x][current_y] = 0
            current_x, current_y = get_prev_coord(current_x, current_y)


if __name__ == '__main__':
    main()
    print(*cells, sep='\n')

