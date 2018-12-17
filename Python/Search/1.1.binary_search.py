# 假设是升序排列的有序列表
def binary_search(obj, item):
    low = 0
    high = len(obj) - 1
    if obj[0] > item or obj[high] < item:
        return None
    while low <= high:
        mid = int(((high - low) / 2) + low)
        if obj[mid] == item:
            # print('index %s is item %s' % (mid, item))
            return obj[mid]
        elif obj[mid] > item:
            # print('%s > item' % mid)
            high = mid - 1
        elif obj[mid] < item:
            # print('%s <= item' % mid)
            low = mid + 1
    return None


# l1 = list(range(0, 100000))

# for i in range(10000):
#     v = binary_search(l1, i)
#     if i != v:
#         print('Error for i = %s and v = %s' % (i, v))
#     else:
#         print('%s -> %s' % (i, v))


l = [1, 4, 6, 7, 8, 22]
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


l2 = [1, 6]
print(binary_search(l2, 6))
print(binary_search(l2, 1))
print(binary_search(l2, 5))

