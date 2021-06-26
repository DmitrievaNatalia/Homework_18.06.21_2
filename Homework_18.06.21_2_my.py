import os
import operator
import pathlib
from pathlib import Path


def files_sorted_by_sizes(path):
    """This function gets file catalog's path and return the list of catalog's files sorted by size"""
    names = os.listdir(path)
    files_list = [os.path.join(path, name) for name in names]
    files_sizes = {path: os.stat(path).st_size for path in files_list}
    sorted_files_sizes = sorted(files_sizes.items(), key=operator.itemgetter(1))
    m = []
    for item in sorted_files_sizes:
        m.append(item[0])
    return m


print(files_sorted_by_sizes("C:\Python\Homework_18.06.21_2\data"))


def join_files_to_new(ls):
    for i in ls:
        with open(i, 'r', encoding='utf-8') as reader, open('result.txt', 'a', encoding='utf-8') as writer:
            s = reader.readlines()
            writer.writelines((f'{i[-5]}\n'))
            writer.writelines(s)
            writer.writelines('\n')

join_files_to_new(files_sorted_by_sizes("C:\Python\Homework_18.06.21_2\data"))