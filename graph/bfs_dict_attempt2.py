# !breadth first search !dfs !graph

# dict of nodes as the key and sets for the edges(children) 
graph = {'A': set(['B', 'C', 'D']),
		 'B': set(['E', 'F']),
		 'C': set([]),
		 'D': set(['G', 'H']),
		 'E': set([]),
		 'F': set(['I', 'J']),
		 'G': set(['K']),
		 'H': set([]),
		 'I': set([]),
		 'J': set([]),
		 'K': set([])}

def bfs(graph, start):
	visited = set()
	queue = [start]
	search_order = []
	while queue:
		current_node = queue.pop(0)
		if current_node not in visited:
			search_order.append(current_node)
			visited.add(current_node)
			queue.extend(graph[current_node] - visited)
	return search_order


searched = bfs(graph, 'A')
assert searched[0] == 'A'
assert sorted(searched[1:4]) == ['B', 'C', 'D']
assert sorted(searched[4:8]) == ['E', 'F', 'G', 'H']
print(searched)

# PSEUDOCODE:
# init visited set
# create a searching queue
# loop while elements are in queue
# pop current node
# if current node not in visited
# add current node to visited
# extend queue with child nodes that are not in visited