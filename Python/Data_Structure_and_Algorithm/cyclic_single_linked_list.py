class LNode():
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

# 这个模型里统一判断条件
# self._rear指向尾节点
# self._rear.next则指向head节点，并没有专门定义一个head
class CSLList():
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self.is_empty():
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    #调用线程方法把元素放到head，
    #然后修改_rear使得hear变成尾节点
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def printall(self):
        if self.is_empty():
            return
        h = self._rear.next
        while True:
            print("elem is ", h.elem, end="\n")
            if h is self._rear:
                break
            h = h.next

cl = CSLList()
cl.prepend(1)
cl.prepend(2)
cl.prepend(3)
cl.prepend(4)
cl.prepend(5)
cl.append(6)
cl.append(7)

cl.printall()










