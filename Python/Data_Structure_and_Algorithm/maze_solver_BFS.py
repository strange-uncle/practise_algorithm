import queue
import pprint
import os
from time import sleep


"""
使用CMD来运行可以看到更好的效果，具体命令参数参见Run Output window.

用队列(FIFO)的方式实现的是 广度优先搜索 BFS(Breadth-first-search).
始终优先考虑最早进入缓存的情况, 是齐头并进的搜索。

"""


def mark(mz: list, pos):
    mz[pos[0]][pos[1]] = 2
    # print('-----------------------------------------------')
    os.system('cls')
    pretty_print_maze(mz)
    sleep(0.3)


def passable(mz: list, pos):
    return mz[pos[0]][pos[1]] == 0


def maze_solver_breadth_first_search(mz: list, pos, end):
    pos_queue = queue.Queue()
    pos_queue.put_nowait(pos)
    mark(mz, pos)
    while not pos_queue.empty():
        current_pos = pos_queue.get_nowait()
        for i in range(4):
            next_pos = (current_pos[0] + directions[i][0], current_pos[1] + directions[i][1])
            if passable(mz, next_pos):
                if next_pos == end:
                    print('Done.')
                    return True
                mark(mz, next_pos)
                pos_queue.put_nowait(next_pos)
    print('Not found path.')
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
    st_pos_backtracking = queue.LifoQueue()
    # 方向顺序是 上下左右。
    # 可以使用下表0，1，2，3来代表每个方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start_pos = (1, 1)
    end_pos = (11, 9)
    maze_solver_breadth_first_search(maze, start_pos, end_pos)
    pretty_print_maze(maze)
