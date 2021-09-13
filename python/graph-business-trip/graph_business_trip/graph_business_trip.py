from .qeue import *

class Vertices:
    def __init__(self, data):
        self.data = data

    def __str__(self):
      return self.data

class Edge:
  def __init__(self,vertices ,weight=1):
        self.vertices = vertices
        self.weight = weight
class Graph:
    def __init__(self ):
        self.graph = {}

    def add_vertices(self, value):
      node = Vertices(value)
      self.graph[node] = []
      return node

    def add_edge(self, v1, v2,weight = 1):
        if v1 in self.graph and v2 in self.graph:
          edge1 = Edge(v2,weight)
          self.graph[v1].append(edge1)

          edge2= Edge(v1,weight)
          self.graph[v2].append(edge2)


    def get_nodes(self):
      return self.graph.keys()

    def get_neighbors(self, node):

      return self.graph.get(node,[])

    def size(self):
      return len(self.graph)

    def breadth_first(self,vertex):
        nodes =  list()
        breadth =  Queue()
        visited =  set()

        breadth.enqueue(vertex)
        visited.append(vertex)

        while breadth:
            front = breadth.dequeue()
            nodes.append(front)

            for child in self.graph.get(front):
                if(child.vertex not in visited):
                    visited.append(child)
                    breadth.enqueue(child)

        return nodes

def business_trip(graph, city_names):
        keys = list(graph.get_nodes())
        city = 0

        for trip in city_names:
            if trip in keys:
                city+=1
        if city != len(city_names):
            return [False,0]

        neighbors = graph.get_neighbors(city_names[0])
        weight = 0
        for value in neighbors:
            if value.vertex.data in city_names[1:]:
                 weight+=value.weight
        if weight != 0:
            return [True,weight]

        return [False,0]



if __name__ == '__main__':
  graph = Graph()
  v1 = graph.add_vertices(9)
  v2 = graph.add_vertices(5)
  v3 = graph.add_vertices(3)
  graph.add_edge(v1, v2)
  print(graph.get_nodes)
  print(graph.get_neighbors)
