import pprint
import os
from time import sleep


"""
使用CMD来运行可以看到更好的效果，具体命令参数参见Run Output window.

用递归的方式是属于 DFS (Depth-first-search) 深度优先搜索.

注意，下面三个步骤演示了递归之美：如果某个方向没路了，递归调用栈会依次回退到以前的可用状态。
这就是递归调用的特点, 这需要仔细体会。
@符号所在位置是我特意标注的关键回退点。

1. 到了倒数第二行的第三列
----------------------------------------
x  x  x  x  x  x  x  x  x  x  x  x  x
x  s  x                             x
x  .  x  x  x     x  x  x     x     x
x  .  .  .  x     x     x     x     x
x  x  x  .  x     x     x     x  x  x
x  .  .  .  x           x           x
x  .  x  x  x  x  x  x  x  x  x     x
x  .  x  .  .  .  x                 x
x  .  x  .  x  .  x     x  x  x     x
x  .  .  .  x  .  x     x           x
x  x  x  x  x  .  x  e  x     x  x  x
x     .  .  .  @        x           x
x  x  x  x  x  x  x  x  x  x  x  x  x

2. 到了倒数第二行的第二列，此时已经无路可走。
所以递归调用栈会一次返回False，直到下图中@符号所在的步骤
----------------------------------------
x  x  x  x  x  x  x  x  x  x  x  x  x
x  s  x                             x
x  .  x  x  x     x  x  x     x     x
x  .  .  .  x     x     x     x     x
x  x  x  .  x     x     x     x  x  x
x  .  .  .  x           x           x
x  .  x  x  x  x  x  x  x  x  x     x
x  .  x  .  .  .  x                 x
x  .  x  .  x  .  x     x  x  x     x
x  .  .  .  x  .  x     x           x
x  x  x  x  x  .  x  e  x     x  x  x
x  .  .  .  .  @        x           x
x  x  x  x  x  x  x  x  x  x  x  x  x

3. @符号所在的步骤的‘向左’移动最终获得了False，所以尝试其他的移动方向，只能是‘向右’移动，结果评估可行！
继续走下去就能找到 end_pos了。
----------------------------------------
x  x  x  x  x  x  x  x  x  x  x  x  x
x  s  x                             x
x  .  x  x  x     x  x  x     x     x
x  .  .  .  x     x     x     x     x
x  x  x  .  x     x     x     x  x  x
x  .  .  .  x           x           x
x  .  x  x  x  x  x  x  x  x  x     x
x  .  x  .  .  .  x                 x
x  .  x  .  x  .  x     x  x  x     x
x  .  .  .  x  .  x     x           x
x  x  x  x  x  .  x  e  x     x  x  x
x  .  .  .  .  @  .     x           x
x  x  x  x  x  x  x  x  x  x  x  x  x
----------------------------------------
"""

def mark(mz: list, pos):
    mz[pos[0]][pos[1]] = 2
    os.system('cls')
    pretty_print_maze(mz)
    sleep(0.5)


def passable(mz: list, pos):
    return mz[pos[0]][pos[1]] == 0


def find_path(mz: list, pos, end):
    mark(mz, pos)
    if pos == end:
        # find the end point
        return True
    for direction in directions:
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if passable(mz, next_pos):
            if find_path(mz, next_pos, end):
                return True
    return False


def pretty_print_maze(mz: list):
    """
    # pretty print the maze
    :param mz: the list that stands for the maze board
    :return: void.
    """
    for row in range(len(mz)):
        for column in range(len(mz[0])):
            if start_pos == (row, column):
                print(' S ', end='')
            elif end_pos == (row, column):
                print(' E ', end='')
            elif mz[row][column] == 1:
                print(' x ', end='')
            elif mz[row][column] == 0:
                print('   ', end='')
            elif mz[row][column] == 2:
                print(' . ', end='')
        print()
        
        
if __name__ == '__main__':
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    # offset for top, bottom, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start_pos = (1, 1)
    end_pos = (10, 7)
    r = find_path(maze, start_pos, end_pos)
    if r:
        print('Find the  path')
    else:
        print('Didn\'t find the  path')
    
    # pretty_print_maze(maze)


