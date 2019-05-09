# coding=UTF-8
# n个人围成一圈，从第k个人开始报数，报到第m个人的时候此人退出。然后从下一个人开始继续报数并按同样的规则退出。
# 直到所有人退出。
# 结果：按照顺序输出每个退出人的编号。

def josephus_mark_elem(total_person: int, start_person: int, period: int):
	if total_person <= 0 or start_person <= 0 or period <= 0:
		raise ValueError("parameters cannot be 0")
	crt_index = start_person - 1
	person_list = list(range(1, total_person + 1))
	for remain_person in range(total_person, 0, - 1):
		p = 0
		while p < period:
			if person_list[crt_index] > 0:
				p += 1
			if p == period:
				print("mark person is ", person_list[crt_index])
				person_list[crt_index] = 0
			# 千万小心，这个方法只标记0，不delete，所以下面始终是 % total_person
			# 最后一次while循环的时候，person_list[crt_index]已经被设置成0了，
			# 所以设置下面的代码不会影响后续for循环里初始的状态
			crt_index = (crt_index + 1) % total_person
			
	
def josephus_delete_elem(total_person: int, start_person: int, pop_number: int):
	if total_person <= 0 or start_person <= 0 or pop_number <= 0:
		raise ValueError("parameters cannot be 0")
	input = list(range(1, total_person + 1))
	crt_idx= start_person - 1
	for remain_person in range(total_person, 0, -1):
		crt_idx = (crt_idx + pop_number - 1) % remain_person
		print("josephus_delete_elem 0 pop item value is ", input.pop(crt_idx))

if __name__ == '__main__':
	josephus_delete_elem(7, 2, 30)
	josephus_mark_elem(7, 2, 30)
	