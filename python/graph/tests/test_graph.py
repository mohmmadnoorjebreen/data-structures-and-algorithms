from graph import __version__

from graph.graph import *
def test_version():
    assert __version__ == '0.1.0'

def test_Node_can_be_successfully_added_to_the_graph():
    graph = Graph()
    graph.add_node('a')
    expected = []
    actual =graph.graph.get('a')
    assert actual == expected


def test_An_edge_can_be_successfully_added_to_the_graph():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('a','b')
    expected = ['b',1]
    value =[graph.graph.get('a')]
    actual = [value[0][0][0].vertex,value[0][0][1]]
    assert actual == expected

def test_All_appropriate_neighbors_can_be_retrieved_from_the_graph():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('a','b')
    expected = [['b',1]]
    actual = graph.get_neighbors('a')
    assert expected == actual

def test_The_proper_size_is_returned_representing_the_number_of_nodes_in_the_graph():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert expected == actual



def test_The_proper_size_is_returned_representing_the_number_of_nodes_in_the_graph():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert expected == actual


def test_An_empty_graph_properly_returns_null():
    graph = Graph()
    expected = None
    actual = graph.get_nodes()
    assert expected == actual
