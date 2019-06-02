# !depth first search !dfs !graph

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

def dfs(graph, start):
	visited = set()
	stack = [start]
	while stack:
		current_node = stack.pop()
		print('visiting node ', current_node)
		visited.add(current_node)
		stack.extend(graph[current_node] - visited)


dfs(graph, 'A')

# PESUDOCODE
# create set of visited nodes
# create a searching stack with the starting node
# while the stack has nodes
# pop the current_node off of the stack
# add current node to visited
# add the connected nodes minus visitsed to the stack to search