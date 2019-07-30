import queue

"""
. 是最终走过的路， - 是走过但被证明是错误的路。
Done.
 x  x  x  x  x  x  x  x  x  x  x  x  x
 x  s  x  -  -  -  -  -  -  -  -  -  x
 x  .  x  x  x  -  x  x  x  -  x  -  x
 x  .  .  .  x  -  x  -  x  -  x  -  x
 x  x  x  .  x  -  x  -  x  -  x  x  x
 x  .  .  .  x  -  -  -  x  -  -  -  x
 x  .  x  x  x  x  x  x  x  x  x  -  x
 x  .  x  .  .  .  x  .  .  .  .  .  x
 x  .  x  .  x  .  x  .  x  x  x  .  x
 x  .  .  .  x  .  x  .  x  .  .  .  x
 x  x  x  x  x  .  x  .  x  .  x  x  x
 x  -  -  -  -  .  .  .  x  e  0  0  x
 x  x  x  x  x  x  x  x  x  x  x  x  x

"""


def mark(mz: list, pos):
    mz[pos[0]][pos[1]] = 2
    

def passable(mz: list, pos):
    return mz[pos[0]][pos[1]] == 0


def pretty_print_maze(mz: list, st: queue.LifoQueue):
    lst_history = list()
    while not st.empty():
        lst_history.append(st.get()[0])
    for row in range(len(mz)):
        for column in range(len(mz[0])):
            if start_pos == (row, column):
                print(' s ', end='')
            elif end_pos == (row, column):
                print(' e ', end='')
            elif mz[row][column] == 1:
                print(' x ', end='')
            elif (row, column) in lst_history:
                print(' . ', end='')
            elif mz[row][column] == 0:
                print(' 0 ', end='')
            elif mz[row][column] == 2:
                print(' - ', end='')
        print()


def maze_solver_backtracking(mz: list, pos, end):
    if pos == end:
        print('Done.')
        return True
    mark(mz, pos)
    st_pos_backtracking.put((pos, int(0)))
    while not st_pos_backtracking.empty():
        pop_pos, direction = st_pos_backtracking.get()
        for i in range(direction, 4):
            next_pos = (pop_pos[0] + directions[i][0], pop_pos[1] + directions[i][1])
            if next_pos == end:
                # 把终点之前的最后一步回填到stack里面，不然最后无法打印这最后一步
                st_pos_backtracking.put((pop_pos, i+1))
                print('Done.')
                return True
            elif passable(mz, next_pos):
                st_pos_backtracking.put((pop_pos, i+1))
                mark(mz, next_pos)
                st_pos_backtracking.put((next_pos, 0))
                break
    print('No path found.')
    return False


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
    maze_solver_backtracking(maze, start_pos, end_pos)
    pretty_print_maze(maze, st_pos_backtracking)
