# Python program to print all paths from a source to destination.

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	def __init__(self, vertices):
		# No. of vertices
		self.V = vertices
		
		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	'''A recursive function to print all paths from 'u' to 'd'.
	visited[] keeps track of vertices in current path.
	path[] stores actual vertices and path_index is current
	index in path[]'''
	def printAllPathsUtil(self, u, d, visited, path):

		# Mark the current node as visited and store in path
		visited[u]= True
		path.append(u)

		# If current vertex is same as destination, then print
		# current path[]
		if u == d and len(path) == 18:
			print (path)
		else:
			# If current vertex is not destination
			# Recur for all the vertices adjacent to this vertex
			for i in self.graph[u]:
				if visited[i]== False:
					self.printAllPathsUtil(i, d, visited, path)
					
		# Remove current vertex from path[] and mark it as unvisited
		path.pop()
		visited[u]= False


	# Prints all paths from 's' to 'd'
	def printAllPaths(self, s, d):

		# Mark all the vertices as not visited
		visited =[False]*(self.V)

		# Create an array to store paths
		path = []

		# Call the recursive helper function to print all paths
		self.printAllPathsUtil(s, d, visited, path)



# Create a graph given in the above diagram
g = Graph(18)
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 3)
g.addEdge(4, 5)
g.addEdge(5, 4)
g.addEdge(6, 7)
g.addEdge(7, 6)
g.addEdge(7, 8)
g.addEdge(8, 7)
g.addEdge(8, 9)
g.addEdge(9, 8)
g.addEdge(9, 10)
g.addEdge(10, 9)
g.addEdge(10, 11)
g.addEdge(11, 10)
g.addEdge(12, 13)
g.addEdge(13, 12)
g.addEdge(13, 14)
g.addEdge(14, 13)
g.addEdge(14, 15)
g.addEdge(15, 14)
g.addEdge(15, 16)
g.addEdge(16, 15)
g.addEdge(16, 17)
g.addEdge(17, 16)

g.addEdge(0, 6)
g.addEdge(6, 0)
g.addEdge(1, 7)
g.addEdge(7, 1)
g.addEdge(2, 8)
g.addEdge(8, 2)
g.addEdge(3, 9)
g.addEdge(9, 3)
g.addEdge(4, 10)
g.addEdge(10, 4)
g.addEdge(5, 11)
g.addEdge(11, 5)
g.addEdge(6, 17)
g.addEdge(17, 6)
g.addEdge(7, 16)
g.addEdge(16, 7)
g.addEdge(8, 15)
g.addEdge(15, 8)
g.addEdge(9, 14)
g.addEdge(14, 9)
g.addEdge(10, 13)
g.addEdge(13, 10)
g.addEdge(11, 12)
g.addEdge(12, 11)

s = 0 ; d = 17
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)
# This code is contributed by Neelam Yadav
