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
		
# 练习使用stack来检查输入的文本里包含的括号是否配对
def next_parenthese(text: str, all_parens: str):
    for i in range(len(text)):
        if text[i] not in all_parens:
            continue
        yield text[i]


def validate_parenthesis(s: str):
    all_parens = "()[]{}"
    open_parens = "([{"
    parens_dict = {")":"(","]":"[","}":"{"}

    st = SStack()
    for t in next_parenthese(s, all_parens):
        if t in open_parens:
            st.push(t)
            continue
        # in case the first parens char is not open parens which will cause stack under flow error
        if st.is_empty():
            print("error when current item is ", t, " and previous item is None")
            return
        # may need print the v later; otherwise the code can be simple like : elif parens_dict[t] != st.pop():
        v = st.pop()
        if parens_dict[t] != v:
            print("error when current item is ",t, " and previous item is ", v)
            return
    if not st.is_empty():
        print("error, some open parens are remaining in the stack")
        while not st.is_empty():
            print(st.pop())
        return
    print("Done with no error.")


# 根据输入的数字和+-*/来计算表达式的值。
# 注意，这里支持的是“后缀表达式” suffix expression
# 比如“1 2 + 3 * ” 代表的是 1 + 2，算出来的结果再 * 3，即 （1+2）*3
class ESStack(SStack):
    def depth(self):
        return len(self._elem)

def suffix_exp_calculator(txt: 'str'):
    op_list = ['+','-','*','/']
    ls = txt.split()
    st = ESStack()
    # ['1', '2', '+', '3', '+', '4', '-']
    for i in ls:
        if i not in op_list:
            st.push(float(i))
            continue
        if i in op_list:
            if st.depth() < 2:
                raise StackUnderFlow("error before pop a and b in suffix_exp_calculator")
            a = st.pop()
            b = st.pop()
            if i == '+':
                st.push(b + a)
            elif i == '-':
                st.push(b - a)
            elif i == '*':
                st.push(b * a)
            elif i == '/':
                st.push(b / a)
            else:
                break
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Process incomplete.")


def covert_infix_to_suffix(txt: 'str') -> 'str':
    """
    ( 3 - 5 ) * ( 6 * 17 - 4 ) / 3  and result is:  3 5 - 6 17 * 4 - * 3 /
    ( 3 - 5 ) * ( 6 + 17 / 4 ) / 3  and result is:  3 5 - 6 17 4 / + * 3 /

    :param txt:( 3 - 5 ) * ( 6 * 17 - 4 ) / 3
    :return:3 5 - 6 17 * 4 - * 3 /
    """
    exp = []
    st = ESStack()
    op_list = ['+','-','*','/','(',')']
    priority = {"(": "1", "+": "2", "-": "2", "*": "3", "/": "3"}
    for i in txt.split():
        if i not in op_list:
            exp.append(i)
        elif i == '(':
            st.push(i)
        elif i == ')':
            while st.top() != '(':
                exp.append(st.pop())
            # discard the last '('
            st.pop()
        else:
            # ( 3 - 5 ) * ( 6 * 17 - 4 * 3 * 2 * 1 - 1 ) / 3
            # 3 5 - 6 17 * 4 3 2 1 * * * 1 - * 3 /
            while not st.is_empty() and priority[st.top()] >= priority[i]:
                exp.append(st.pop())
            st.push(i)
    
    while not st.is_empty():
        exp.append(st.pop())
        
    return ' '.join(exp)

# practise again in another day
def covert_infix_to_suffix_2(txt: 'str') -> 'str':
    """
    ( 3 - 5 ) * ( 6 * 17 - 4 ) / 3  and result is:  3 5 - 6 17 * 4 - * 3 /
    ( 3 - 5 ) * ( 6 + 17 / 4 ) / 3  and result is:  3 5 - 6 17 4 / + * 3 /

    :param txt:( 3 - 5 ) * ( 6 * 17 - 4 ) / 3
    :return:3 5 - 6 17 * 4 - * 3 /
    """
    op_list = ['+','-','*','/','(']
    op_priority = {'(':'0','+':'1','-':'1','*':'2','/':'2'}
    exp = []
    st = ESStack()
    for c in txt.split(' '):
        if c == '(':
            st.push(c)
        # push numbers
        elif c not in op_list and c != ')':
            exp.append(c)
        elif c in op_list:
            # check priority
            while not st.is_empty() and op_priority[st.top()] >= op_priority[c]:
                exp.append(st.pop())
            st.push(c)
        elif c == ')':
            # logic to check and generate exp
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
            st.pop()
        else:
            pass
    while not st.is_empty():
        exp.append(st.pop())
    return ' '.join(exp)


if __name__ == "__main__":
    # s = SStack()
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # s.push(4)
	#
    # print(s.pop())
    # print(s.top())
    # print(s.pop())
	#
    # l = LStack()
    # l.push(2)
    # l.push(3)
    # l.push(4)
    # l.push(5)
	#
    # print(l.pop())
    # print(l.top())
    # print(l.pop())
    #
    # # revert item in a list by using stack
    # ls = [1,2,3,4,5,6]
    # ss = SStack()
    # ls2 = []
    # for i in ls:
    #     ss.push(i)
    # while not ss.is_empty():
    #     ls2.append(ss.pop())
    #
    # print("after reverted, ls2 items are:")
    # for i in ls2:
    #     print(i)

    #validate_parenthesis("}[)()(a{}}]dsf4)5")

    # txt = '1 2 + 2 3 * 1 - /'
    # txt = '( 3 - 5 ) * ( 6 + 17 / 4 ) - 3'
    txt = '( 3 - 5 ) / ( 6 + 3 * 4 ) - 3'
    # txt = '( 3 - 5 ) * ( 6 * 17 - 4 * 3 * 2 * 1 - 1 ) / 3'
    #a = suffix_exp_calculator(txt)
    #print("calculate: '", txt, "' and the result is: ", a)

    # param txt: txt:(1 + 2) / (2 * 3 - 1)
    # return: 1 2 + 2 3 * 1 - /
    print("trans_infix_suffix is: ", txt, " and result is: ", covert_infix_to_suffix(txt))
    print("covert_infix_to_suffix_2 is: ", txt, " and result is: ", covert_infix_to_suffix_2(txt))
    #( 3 - 5 ) * ( 6 * 17 - 4 ) / 3  and result is:  3 5 - 6 17 * 4 - * 3 /
    #( 3 - 5 ) * ( 6 + 17 / 4 ) / 3  and result is:  3 5 - 6 17 4 / + * 3 /
    # a = suffix_exp_calculator(covert_infix_to_suffix(txt))
    # print("calculate: '", txt, "' and the result is: ", a)

    # ( 3 - 5 ) * ( 6 * 17 - 4 * 3 * 2 * 1 - 1 ) / 3
    # 3 5 - 6 17 * 4 3 * 2 * 1 * - 1 - * 3 /
    
    