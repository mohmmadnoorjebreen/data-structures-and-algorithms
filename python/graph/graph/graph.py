class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self ):
        self.graph = {}

    def add_node(self, vertices):
      node = Node(vertices)
      self.graph[node.vertex] = []


    def add_edge(self, v1, v2,weight = 1):
        if v1 in self.graph and v2 in self.graph:
          node = Node(v2)
          node.next = self.graph[v1]
          value = self.graph.get(v1)
          value.append([node,weight])
          self.graph[v1] = value
          node = Node(v1)
          node.next = self.graph[v2]
          value = self.graph.get(v2)
          value.append([node,weight])
          self.graph[v2] = value

    def get_nodes(self):
      nodes = []
      for node in self.graph.keys():
        nodes.append(node)
      if nodes == [] :
        return None
      return nodes

    def get_neighbors(self, node):
      neighbors = []
      for value in self.graph.get(node):
        neighbors.append([value[0].vertex,value[1]])
      return neighbors

    def size(self):
      num = 0
      for _ in self.graph.keys():
        num += 1
      return num



