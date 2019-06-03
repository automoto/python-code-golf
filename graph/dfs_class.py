"""
You are given a Node class that has a name and an array of optional children Nodes. When put together, 
Nodes form a simple tree-like structure. Implement the breadthFirstSearch method on the Node class, 
which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right),
stores all of the Nodes' names in the input array, and returns it.


"""
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
    	stack = [self]
    	while stack:
    		current_node = stack.pop()
    		array.append(current_node.name)
    		for child in current_node.children:
    			queue.append(child)
    	return array