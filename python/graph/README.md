# Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list


## Approach & Efficiency
Simple, quick and direct Approach have been taken


## API

1. add node

Arguments: value

Returns: The added node

Add a node to the graph

2. add edge

Arguments: 2 nodes to be connected by the edge, weight (optional)

Returns: nothing

Adds a new edge between two nodes in the graph

If specified, assign a weight to the edge

Both nodes should already be in the Graph

3. get nodes

Arguments: none

Returns all of the nodes in the graph as a collection (set, list, or similar)

4. get neighbors

Arguments: node

Returns a collection of edges connected to the given node

Include the weight of the connection in the returned collection

5. size

Arguments: none

Returns the total number of nodes in the graph
