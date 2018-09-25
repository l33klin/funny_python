#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 18/09/2018 10:21 PM
@Author  : Jian
@Contact : l33klin@gmail.com
@Site    : 
@File    : big_file_sort.py
"""
import os
import time
import linecache
# from memory_profiler import profile
import tracemalloc


_1KB = 1024
_1MB = _1KB * 1024
_1GB = _1MB * 1024


def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


# @profile
def sort_file(file_name):
    if os.path.getsize(file_name) > 101 * _1MB:
        raise Exception("Too big file")

    split_path = os.path.split(file_name)

    # tracemalloc.start()
    unsorted_list = []
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line or line == "\n":
                break
            number = int(line.strip())
            unsorted_list.append(number)

    start = time.time()
    sorted_list = sorted(unsorted_list)
    end = time.time()
    print("Sorted cost %.4f seconds" % (end - start))

    with open(os.path.join(split_path[0], "sorted_" + split_path[1]), "w") as f:
        for number in sorted_list:
            f.write(str(number) + "\n")

    # snapshot = tracemalloc.take_snapshot()
    # display_top(snapshot)

    return sorted_list


def split_big_file_as_ten(file_name):

    tracemalloc.start()

    _max = 0
    _min = 1000000
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line or line == "\n":
                break
            number = int(line.strip())
            _max = number if _max < number else _max
            _min = number if _min > number else _min

    start_numbers = []
    section_size = int((_max - _min) / 10)

    for i in range(10):
        start_numbers.append(_min + section_size*i)

    with open(file_name, 'r') as f:
        files = []
        try:
            for start_number in start_numbers:
                file = open(os.path.join('data', "start_from_" + str(start_number) + ".data"), 'a')
                files.append(file)

            while True:
                line = f.readline()
                if not line or line == "\n":
                    break
                number = int(line.strip())
                index = int((number - _min)/section_size)

                files[index].write(str(number) + '\n')

        except Exception as e:
            pass
        finally:
            for file in files:
                file.close()

        snapshot = tracemalloc.take_snapshot()
        display_top(snapshot)


if __name__ == '__main__':

    # sort_file("data/start_from_2496.data")
    split_big_file_as_ten("100MB_test.data")
