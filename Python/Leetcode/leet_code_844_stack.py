def backspaceCompare(S: str, T: str) -> bool:
    ST_S = []
    ST_T = []
    for c in S:
        if c == '#':
            if ST_S:
                ST_S.pop()
        else:
            ST_S.append(c)

    for c in T:
        if c == '#':
            if ST_T:
                ST_T.pop()
        else:
            ST_T.append(c)

    return ''.join(ST_S) == ''.join(ST_T)


def backspacecompare_double_point(S: str, T: str) -> bool:
    index_s = len(S) - 1
    index_t = len(T) - 1
    cnt_s = 0
    cnt_t = 0

    while index_s >= 0 or index_t >= 0:
        while index_s >= 0 and (S[index_s] == '#' or cnt_s > 0):
            if S[index_s] == '#':
                cnt_s += 1
            else:
                cnt_s -= 1
            index_s -= 1
        while index_t >= 0 and (T[index_t] == '#' or cnt_t > 0):
            if T[index_t] == '#':
                cnt_t += 1
            else:
                cnt_t -= 1
            index_t -= 1

        if index_s < 0 or index_t < 0:
            return index_s == index_t

        if S[index_s] != T[index_t]:
            return False

        index_s -= 1
        index_t -= 1

    return index_s == index_t


# print(backspaceCompare2('a###bcd#e', 'bce'))
print(backspacecompare_double_point('a#bc##de#f','dff#f#'))
