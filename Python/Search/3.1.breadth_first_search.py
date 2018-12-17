from collections import deque


if __name__ == "__main__":
    search_deque = deque()
    ## 确保只检查一次，否则可能出现循环引用导致的死循环，如a->b, b->a的情况
    searched_list = []
    graph = {}
    graph['me'] = ["a","b","c"]
    graph['a'] = ["a2", "A3", "a4","b"]
    graph['b'] = ["b2", "b3", "b4","a"]
    graph['c'] = ["CC", "Win", "CCCC"]

    graph['a2'] = []
    graph['A3'] = []
    graph['a4'] = []

    graph['b2'] = ['213Win']
    graph['b3'] = ['Win123']
    graph['b4'] = ['666']
    graph['213Win'] = []
    graph['Win123'] = []
    graph['666'] = []

    graph['CC'] = []
    graph['Win'] = []
    graph['CCCC'] = []

    search_deque += graph["me"]
    while search_deque:
        p = search_deque.popleft()
        if p not in searched_list:
            if p == 'b3':
                print('p is b3, done.')
                break
            else:
                print('P is %s and lose' % p)
                search_deque += graph[p]
                searched_list.append(p)
