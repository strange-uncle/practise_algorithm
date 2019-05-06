import linear_list as ll


class DLNode(ll.LNode):
    def __init__(self, elem, next_ = None, prev = None):
        ll.LNode.__init__(self, elem, next_)
        self.prev = prev


class DLList(ll.LList_rear):
    def __init__(self):
        ll.LList_rear.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, self._head, None)
        if self._head is None:
            self._rear = p
        else:
            self._head.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, None, self._rear)
        if self._head is None:
            self._head = p
        else:
            self._rear.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise ValueError("head is None in pop")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise ValueError("head is None in pop")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e











