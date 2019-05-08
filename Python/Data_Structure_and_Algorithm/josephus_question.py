# coding=UTF-8
# n个人围成一圈，从第k个人开始报数，报到第m个人的时候此人退出。然后从下一个人开始继续报数并按同样的规则退出。
# 直到所有人退出。
# 结果：按照顺序输出每个退出人的编号。


def josephus_mark_elem(total_person: int, start_person: int, pop_number: int):
	if total_person <= 0 or start_person <= 0 or pop_number <= 0:
		raise ValueError("parameters cannot be 0")
	crt_index = start_person - 1
	input = list(range(1, total_person + 1))
	for remain_item in range(total_person, 0, -1):
		valid_count = 0
		inc = 0
		while valid_count < pop_number:
			# 千万小心，这个方法只标记0，不delete，所以下面始终是 % total_person
			crt_index = (crt_index + inc) % total_person
			if input[crt_index] == 0:
				pass
			else:
				valid_count += 1
			inc = 1
		print("josephus_mark_elem - pop item value is ", input[crt_index])
		input[crt_index] = 0
	
def josephus_delete_elem(total_person: int, start_person: int, pop_number: int):
	if total_person <= 0 or start_person <= 0 or pop_number <= 0:
		raise ValueError("parameters cannot be 0")
	input = list(range(1, total_person + 1))
	crt_idx= start_person - 1
	for remain_person in range(total_person, 0, -1):
		crt_idx = (crt_idx + pop_number - 1) % remain_person
		print("josephus_delete_elem 0 pop item value is ", input.pop(crt_idx))

if __name__ == '__main__':
	josephus_delete_elem(4, 2, 5)
	josephus_mark_elem(4, 2, 5)
