# 假设是升序排列的有序列表
def binary_search(obj, item):
    low = 0
    high = len(obj) - 1
    if obj[0] > item or obj[high] < item:
        return None
    while True:
        guess = int(((high - low) / 2) + low)
        if obj[guess] == item:
            print('%s == item' % guess)
            return guess
        elif obj[guess] > item:
            print('%s > item' % guess)
            high = guess - 1
        elif obj[guess] < item:
            print('%s <= item' % guess)
            low = guess + 1


l = list(range(0, 100000))

# for i in range(10000):
#     v = binary_search(l, i)
#     if i != v:
#         print('Error for i = %s and v = %s' % (i, v))
#     else:
#         print('%s -> %s' % (i, v))

print(binary_search(l, 100000-1))
