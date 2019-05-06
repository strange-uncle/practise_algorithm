# coding=UTF-8
class LNode():
	def __init__(self, elem, next_ = None):
		self.elem = elem
		self.next = next_

# h = LNode(1)
# h.next = LNode(2)
# h.next.next = LNode(3)
# h.next.next.next = LNode(4)

## 定义head变量，它指向表里的第一个元素，这时候元素的顺序是 1，2，3，4
# head = h

## 1. 表首端的插入,完成以后这head的元素顺序是10，1，2，3，4
# n1 = LNode(10)
# n1.next = head
# head = n1

## 2. 插入到2和3中间，完成以后head的元素顺序就是10,1,2,11,3,4
## 定义pre就是插入位置的前一个元素
# n2 = LNode(11)
# pre = head.next.next
# n2.next = pre.next
# pre.next = n2


## 3. 删除中间元素，比如删除2,那么pre就是2前面的元素
## 删除完毕以后，元素顺序是10,1,11,3,4
# pre = head.next
# pre.next = pre.next.next
#

## 4. 得到第4个元素,或者说下标=3的元素.下标从0开始.
# i = 4
# p = head
# while p is not None and i > 0:
# 	i -= 1
# 	p = p.next
# 	if i == 0:
# 		print("index = 3, value = ", p.elem)
#

class LinkedListUnderflow(ValueError):
	pass


class LList():
	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head is None

	def prepend(self, elem):
		self._head = LNode(elem, self._head)

	def pop(self):
		if self.is_empty():
			raise LinkedListUnderflow("pop - list is empty")
		q = self._head.elem
		self._head = self._head.next
		return q

	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem)
			return
		h = self._head
		while h.next is not None:
			h = h.next
		h.next = LNode(elem)

	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow("pop_last -> head is None")
		n, q = self._head, None
		if n.next is None:
			q = n.elem
			self._head = None
			return q
		while n.next.next is not None:
			n = n.next
		q = n.next.elem
		n.next = None
		return q

	def __str__(self):
		s = ""
		q = self._head
		while q is not None:
			s += "," + str(q.elem)
			q = q.next
		return s

	def print_all(self):
		p = self._head
		while p is not None:
			print(p.elem, end='')
			if p.next is not None:
				print(',', end='')
			p = p.next
		print('')
	# 生成器函数
	def elements(self):
		p = self._head
		while p is not None:
			yield p.elem
			p = p.next

	def reverse(self):
		prev_node = None
		while self._head is not None:
			h = self._head
			self._head = h.next
			h.next = prev_node
			prev_node = h
		self._head = prev_node


class LList_rear(LList):
	def __init__(self):
		LList.__init__(self)
		self._rear = None

	def prepend(self, elem):
		if self._head is None:
			self._head = LNode(elem, None)
			self._rear = self._head
		else:
			self._head = LNode(elem, None)

	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem, None)
			self._rear = self._head
		else:
			self._rear.next = LNode(elem, None)
			self._rear = self._rear.next

if __name__ == "__main__":
	l = LList()
	for i in range(10):
		l.prepend(i)

	# l.append(666)
	# print("before pop_last:",l)
	# print(l.pop_last())
	# print(l.pop_last())
	# print("after pop_last:",l)

	l.print_all()
	l.reverse()
	l.print_all()

























