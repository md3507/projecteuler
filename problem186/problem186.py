'''
Problem 186

@author Mark Dijkstra
'''


S = {} #dictionary of lagged fibonacci generator
records = {}
def record(k):
	if (k <= 55):
		S[k] = ((100003 - ( 200003*k )  + ( 300007*(k**3))) % 1000000) 
	else:
		S[k] = (S[k - 24] + S[k - 55]) % 1000000

"""


class Graph(object):
	''' Graph used for problem 186 ''' 
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg


	def add_node(self, node):

	def depth_first_search(self):

	def strongly_connected_components(self):


class Node(object):
	''' Node object for the graph class ''' 
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
"""

if __name__ == "__main__":
	for i in range(1,100000000):
		record(i)
		x = S[i]
		print(i, x)
		if (x == 524287):
			print(i)
			break
