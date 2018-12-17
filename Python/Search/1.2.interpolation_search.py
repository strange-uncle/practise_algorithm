'''
经过分析,这种插值查找的代码实现起来容易出错, 然后应用范围也比较窄.
不是必要的情况就尽量不用.

在完全均匀的列表里面,循环里面执行1次查找即可找到.
如果v不在列表里面,执行完毕第一次循环后,在第二次循环的判断条件里面即可判断不存在然后退出.


插值查找(Interpolation Search),这是二分查找的一个特殊优化版本,
针对的是数据分布平均的有序列表.
[1,2,3,4,5]和[1,3,5,7,9]这种就是平均分布的, 列表内部相邻的两个元素的增量都是恒定的.
而[1,2,4,8,16,32]这就不是平均分布的列表.

换句话说,用X,Y轴来画图,画出来是一条直线的才是平均分布.

0. 如果v等于list[low] 或者 list[high],那么直接返回对应的值.
1. 如果v小于list[low] 或者大于 list[high],那么不存在列表里面.

2. 分析数据存在列表里面的情况:

先假设有一个完全均匀分布的有序列表: [1,2,3,4,5,6,7,8,9,10],
如果要查找v = 4那么下意识就知道应该在这个列表的前面部分去找,
不需要再从列表的中间元素去找.

具体v = 4的大概位置可以这样来计算:

把列表想象成为一个线条,考虑v在这个'线条'中间的某个位置,然后看list[low]~v 这段'线条'占据了整个'线条'的多少比例:
    (v - list[low])/(list[high] - list[low])
因为这个列表是均匀分布的, 那么这个比例就可以表达v到底在这个列表list[low]后面的哪个位置.
注意关键点'list[low]后面'.
    (4 - 1)/(10 - 1) = 3/9 = 1/3

考虑从list[v] 到 list[high]这些数据为一个子列表.
既然这个列表是均匀分布的,那么某个v值占据 子列表 里面值(2~10)的比例, 就等于某个v值的index占据 子列表 里面index(index是1~9)的比列.

最终的位置要加上low,计算出来是:
    given low = 0, high = 9

    low + (high - low)*((v - list[low])/(list[high] - list[low]))
    = 0 + 9 * (1/3)
    = 0 + 3
    = 3


3. 分析数据不存在列表中间的情况:

先假设有一个'基本上'均匀分布的有序列表: [1,2,3,  5,6,7,  8,9,10], 这次待查的v = 4.

看下#2的结论是否还有效.
    given low = 0, high = 8

    low + (high - low)*((v - list[low])/(list[high] - list[low]))
    = 0 + 8 * ((4 - 1)/(10 - 1))
    = 0 + 8 * 3/9
    = 0 + 2.666666667
    = 2

结果list[2] = 3 < 4,必然找不到的.

那么继续走类似二分查找的逻辑.
    low = mid + 1
        = 2 + 1
        = 3

这时候,list[low] = 5 已经在v = 4的后面了,肯定找不到4了噻!

试着强制计算一波:
    given low = 3, high = 8

    low + (high - low)*((v - list[low])/(list[high] - list[low]))
    = 3 + (8 - 3) * ((4 - 5)/(10 - 5))
    = 3 + 5 * (-1/5)
    = 3 - 1
    = 2

low又回到2了,如果继续跑下去,就是死循环了.
所以WHILE判断条件要有list[low] < v.
并且WHILE判断条件还要考虑分母不为0,那么(list[high] - list[low]) != 0,

'''


def fn_interpolation_search(obj, v):
    low = 0
    high = len(obj) - 1
    if v < obj[low] or v > obj[high]:
        return None
    if v == obj[low]:
        return low
    if v == obj[high]:
        return high

# 经过测试,发现一个情况,经过移动以后 obj[low]或者obj[high]有可能等于v.
# 所以判断v值的范围要加上=
    while obj[low] <= v <= obj[high] and obj[low] < obj[high]:
        mid = int(low + (high - low)*((v - obj[low])/(obj[high] - obj[low])))
        if obj[mid] == v:
            print('mid is %s = v is %s' % (mid, v))
            return mid
        elif obj[mid] > v:
            print('mid is %s > v is %s' % (mid, v))
            high = mid - 1
        elif obj[mid] < v:
            print('mid is %s < v is %s' % (mid, v))
            low = mid + 1
    return None


# 测试比较均匀的分布
# l = [1,2,3,  5,6,7,  8,9,10]
# print(fn_interpolation_search(l, 8))

# 测试完全均匀的分布
# l = [6,6,6,6,6,6,6,6,6,6]
# print(fn_interpolation_search(l, 6))

# 再次测试完全均匀的分布
l = [2,4,6,8,10,12,14,16,18,20,22]
print(fn_interpolation_search(l, 16))
