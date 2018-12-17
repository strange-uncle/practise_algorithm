import queue

findNums = [4,1,2]
nums = [6,5,4,3,7,1] ##[1,3,4,2]

d = {}
ans = [-1] * len(findNums)
for i, num in enumerate(findNums):
    d[num] = i

stack = []
for num in nums:
    while stack and stack[-1] < num:
        top = stack.pop()
        if top in d:
            ans[d[top]] = num
    stack.append(num)

print(ans)

stack = queue.LifoQueue()
stack.put(None)

