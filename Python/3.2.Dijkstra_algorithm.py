from collections import deque


graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5
graph["end"] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = float("inf")

parents = {}
parents['a'] = "start"
parents['b'] = 'start'
parents['end'] = None

processed = []

def find_lowest_node(costs):
    lowest_costs = float('inf')
    lowest_costs_node = None
    for c in costs.keys():
        if costs[c] < lowest_costs and c not in processed:
            lowest_costs = costs[c]
            lowest_costs_node = c
    return lowest_costs_node

node = find_lowest_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_costs = cost + neighbors[n]
        if costs[n] > new_costs:
            costs[n] = new_costs
            parents[n] = node
    processed.append(node)
    node = find_lowest_node(costs)

for k,v in parents.items():
    print("%s comes from %s" % (k, v))

print('*'*20)
for k,v in costs.items():
    print(k,v)


