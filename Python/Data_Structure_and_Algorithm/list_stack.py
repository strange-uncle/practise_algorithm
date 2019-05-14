# coding=utf-8

class StackUnderFlow(ValueError):
	pass

# based on sequence list
class SStack():
	def __init__(self):
		self._elem = []
	
	def is_empty(self):
		return len(self._elem) == 0
	
	def pop(self):
		if self.is_empty():
			raise StackUnderFlow("error when pop")
		return self._elem.pop()
	
	def push(self, elem):
		self._elem.append(elem)
	
	def top(self):
		if self.is_empty():
			raise StackUnderFlow("error when top")
		return self._elem[-1]

class LNode():
	def __init__(self, elem, next_ = None):
		self.elem = elem
		self.next = next_


# based on linked list: LNode
class LStack():
	def __init__(self):
		self._top = None
	
	def is_empty(self):
		return self._top is None
		
	def pop(self):
		if self.is_empty():
			raise StackUnderFlow("error in LStack - pop()")
		p = self._top
		self._top = p.next
		return p.elem
	
	def push(self, elem):
		self._top = LNode(elem, self._top)
	
	def top(self):
		if self.is_empty():
			raise StackUnderFlow("error in LStack - pop()")
		return self._top.elem
		

if __name__ == "__main__":
	s = SStack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	
	print(s.pop())
	print(s.top())
	print(s.pop())
	
	l = LStack()
	l.push(2)
	l.push(3)
	l.push(4)
	l.push(5)
	
	print(l.pop())
	print(l.top())
	print(l.pop())
