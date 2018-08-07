'''
从列表的第一个元素开始,依次比较相邻的两个元素,如果后面的元素小,那么就交换这两个元素的位置.

第一趟比较完成后,列表的最后一个元素应该就是这个列表里面最大的元素.
第二趟比较还是从第一个元素开始,但最后不用比较列表里的最后一个元素.
第三趟比較完成以后，不用比较列表里面最后的兩个元素.

相当于是说,冒泡是从尾部开始生成有序列表的.

'''

def fn_swap_min(x, y):
    if x > y:
        x, y = y, x
    return x, y

def bubble_sort(obj):
    end_index = len(obj) - 1
    while end_index > 0:
        for i in range(end_index):
            obj[i], obj[i + 1] = fn_swap_min(obj[i], obj[i+1])
        #注意,跑完一趟以后才能设置end_index, 小心不要放到for里面了!
        end_index -= 1
    return obj


l = [10,2,1,7,8,5,3,6,3,21]

print(bubble_sort(l))








