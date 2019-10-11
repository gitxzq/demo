'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-30 15:05:13
@LastEditTime: 2019-10-11 10:29:16
@LastEditors: Never
'''
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('demo\\9.29\\t.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
                print(line, end='')
                print('-' * 20)
