# 假设是升序排列的有序列表
def binary_search(obj, item):
    low = 0
    high = len(obj) - 1
    if obj[0] > item or obj[high] < item:
        return None
    while low <= high:
        guess = int(((high - low) / 2) + low)
        if obj[guess] == item:
            # print('index %s is item %s' % (guess, item))
            return guess
        elif obj[guess] > item:
            # print('%s > item' % guess)
            high = guess - 1
        elif obj[guess] < item:
            # print('%s <= item' % guess)
            low = guess + 1
    return None


# l = list(range(0, 100000))

# for i in range(10000):
#     v = binary_search(l, i)
#     if i != v:
#         print('Error for i = %s and v = %s' % (i, v))
#     else:
#         print('%s -> %s' % (i, v))


l = [1,4,6,7,8,22]
# 不存在的数字
print(binary_search(l, 5))
# 范围之前的数字
print(binary_search(l, -1))
# 范围之后的数字
print(binary_search(l, 30))
# 中间的数字
print(binary_search(l, 7))
# 开始第一位的数字
print(binary_search(l, 1))
# 结尾最后一位的数字
print(binary_search(l, 22))


