import math

graph = {}
graph["start"] = {}

print("estrutura: ",graph)

graph["start"]["a"] = 6
graph["start"]["b"] = 2

print("estrutura: ",graph)
print("estrutura: ",graph['start'])
print("estrutura: ",graph['start']["a"])

print("keys: ", list(graph['start'].keys()))

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

print("estrutura: ",graph)


infinity = math.inf
print(infinity)

costs = {}

costs["a"] = 6
costs["b"] = 2

costs["fin"] = infinity

print(costs)

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

print(parents)

processed = set()

print(processed)

def find_lowest_cost_node(costs):

  lowest_cost = math.inf
  lowest_cost_node=None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost_node = node
  return lowest_cost_node


node = find_lowest_cost_node(costs)
print(node)

while node is not None:
  cost = costs[node]
  print("cost: ", cost)
  neighbors = graph[node]
  for n in neighbors.keys():
    print("neighbor: ", n)
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
  processed.add(node)
  print("Processed: ", processed)
  node = find_lowest_cost_node(costs)

print(parents)

print(costs)
