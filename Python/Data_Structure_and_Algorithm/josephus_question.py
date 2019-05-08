# coding=UTF-8
# n个人围成一圈，从第k个人开始报数，报到第m个人的时候此人退出。然后从下一个人开始继续报数并按同样的规则退出。
# 直到所有人退出。
# 结果：按照顺序输出每个退出人的编号。


def josephus_mark_elem(n: int, k: int, m: int):
	pass

def josephus_delete_elem(n: int, k: int, m: int):
	if n <= 0 or k <= 0 or m <= 0:
		raise ValueError("parameters cannot be 0")
	input = list(range(1, n + 1))
	crt_idx= k - 1
	remain_item = n
	print("Before, ", input)
	for remain_item in range(n, 0, -1):
		crt_idx = (crt_idx + m - 1) % remain_item
		print("pop item is ", input.pop(crt_idx))

if __name__ == '__main__':
	josephus_delete_elem(4, 2, 5)
