# coding=UTF-8
class LNode():
	def __init__(self, elem, next_ = None):
		self.elem = elem
		self.next = next_

h = LNode(1)
h.next = LNode(2)
h.next.next = LNode(3)
h.next.next.next = LNode(4)

## 定义head变量，它指向表里的第一个元素，这时候元素的顺序是 1，2，3，4
head = h

## 1. 表首端的插入,完成以后这head的元素顺序是10，1，2，3，4
n1 = LNode(10)
n1.next = head
head = n1

## 2. 插入到2和3中间，完成以后head的元素顺序就是10,1,2,11,3,4
## 定义pre就是插入位置的前一个元素
n2 = LNode(11)
pre = head.next.next
n2.next = pre.next
pre.next = n2


## 3. 删除中间元素，比如删除2,那么pre就是2前面的元素
## 删除完毕以后，元素顺序是10,1,11,3,4
pre = head.next
pre.next = pre.next.next


## 4. 得到第4个元素,或者说下标=3的元素.下标从0开始.
i = 4
p = head
while p is not None and i > 0:
	i -= 1
	p = p.next
	if i == 0:
		print("index = 3, value = ", p.elem)


class LinkedListUnderflow(ValueError):
	pass


class LList:
	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head is None



print("done")




