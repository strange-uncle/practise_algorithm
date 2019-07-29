"""
简单选择排序 simple selection sort

是从第一个元素开始生成有序列表,和冒泡的方向是相反的.
每一轮比较完成后,只需要交换一次位置.
不像冒泡每次比较都要交换位置.

给定一个无序列表[3,2,1,6,4,5]
定义一个temp变量.temp可以直接保存value, 或者保存成为一个index.
根据具体情况选择.
比如数组是可以根据下表来快速得到value的,那temp就可以保存index;
如果某些链表不方便用下表来得到value,那temp可以考虑保存value.


1. 先赋值temp = 第一个元素的index,即 temp = 0
2. 用obj[temp]和第二个对比,将小的(或者大的)元素的index赋值给temp.
3. 用obj[temp]和第三个对比,将小的(或者大的)元素的index赋值给temp.
...
4. 用obj[temp]和最后一个元素对比完成以后,将整个列表的第一个元素obj[0] 和obj[temp]交换位置.
意思就是说,把这次扫描出来最小(或者最大)的值保存到完整列表的第一个index.
有个坑是, 不能直接赋值,一定要把obj[save_index] 和 obj[temp]交换位置!是交换,不是赋值.

5. 赋值temp = 第二个元素的index,即 temp = 1
6. 类似上面的做法,获取除了第一个元素以后的子列表里面最小的value, 和obj[1]交换位置.

一直这样处理下去,直到temp = len(obj) - 1 就不处理了.

"""


def simple_selection_sort(obj):
    end_index = len(obj) - 1
    temp_index = 0
    save_index = 0
    while save_index < end_index:
        for i in range(save_index, end_index + 1):
            if obj[temp_index] > obj[i]:
                temp_index = i
        obj[save_index], obj[temp_index] = obj[temp_index], obj[save_index]
        save_index += 1
        temp_index = save_index
    return obj


l = [12, 3, 2, 1, 8, 7, 3, 5, 3, 1, 9]
print(simple_selection_sort(l))


