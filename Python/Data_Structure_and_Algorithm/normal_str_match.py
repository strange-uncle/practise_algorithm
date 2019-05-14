# coding=utf-8

# the very basic str match algorithm
def str_first_match(t: str, p: str):
	for i in range(len(t)):
		idx = 0
		while tar[i] == p[idx]:
			if idx == len(p) - 1:
				print("index in target str is ", str(i - idx))
				return
			i += 1
			idx += 1
	print("not found.")
	
if __name__ == "__main__":
	tar = "0123456789"
	p = "678"
	str_first_match(tar, p)

	p = "6780"
	str_first_match(tar, p)
