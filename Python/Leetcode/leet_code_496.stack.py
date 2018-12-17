nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
result = []
for i in range(len(nums1)):
    result.append(-1)
d1 = {}
for k, v in enumerate(nums1):
    d1[v] = k
stack = []

for i in nums2:
    while stack and stack[-1] < i:
        item = stack.pop()
        if item in d1:
            result[d1[item]] = i
    stack.append(i)

print(result)

