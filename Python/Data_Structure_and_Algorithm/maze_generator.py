import random

# find this maze generator on: https://blog.csdn.net/Subson/article/details/86308996
# modify some logic to meet my situation
def maze_gen():
    row, col = 6, 6
    i, j = 0, 0
    
    status = [[[False for _ in range(4)] for _ in range(col)] for _ in range(row)]
    visited = [[False for _ in range(col)] for _ in range(row)]
    
    stack = [(i, j)]
    while stack:
        visited[i][j] = True
        choosable = []
        if j > 0 and not visited[i][j-1]:
            choosable.append('L')
        if i > 0 and not visited[i-1][j]:
            choosable.append('U')
        if j < col-1 and not visited[i][j+1]:
            choosable.append('R')
        if i < row-1 and not visited[i+1][j]:
            choosable.append('D')
        if choosable:
            direct = random.choice(choosable)
            if direct == 'L':
                status[i][j][0] = True
                j -= 1
                status[i][j][2] = True
            elif direct == 'U':
                status[i][j][1] = True
                i -= 1
                status[i][j][3] = True
            elif direct == 'R':
                status[i][j][2] = True
                j += 1
                status[i][j][0] = True
            elif direct == 'D':
                status[i][j][3] = True
                i += 1
                status[i][j][1] = True
            stack.append((i, j))
        else:
            i, j = stack.pop()
    
    maze = [[1 for _ in range(col*2+1)] for _ in range(row*2+1)]
    for r in range(row):
        for c in range(col):
            cell = status[r][c]
            maze[r*2+1][c*2+1] = 0
            if cell[0]:
                maze[r*2+1][c*2] = 0
            if cell[1]:
                maze[r*2][c*2+1] = 0
            if cell[2]:
                maze[r*2+1][c*2+2] = 0
            if cell[3]:
                maze[r*2+2][c*2+1] = 0
    
    print('maze = [')
    for r in range(row*2+1):
        print('    [', end='')
        for c in range(col*2+1):
            if c < col*2:
                print(str(maze[r][c]) + ', ', end='')
            else:
                print(str(maze[r][c]), end='')
        if r < row*2:
            print('],')
        else:
            print(']')
    print(']')


if __name__ == '__main__':
    maze_gen()
