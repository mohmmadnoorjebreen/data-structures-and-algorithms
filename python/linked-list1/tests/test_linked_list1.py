
import pytest

from linked_list1 import __version__

from linked_list1.linked_list import Linked_List , Node

def test_version():
    assert __version__ == '0.1.0'


def test_linkedlist():
   assert Linked_List()

def test_insert_nodes():
  node = Linked_List()
  with pytest.raises(AttributeError):
    node.head.data
  node.insert(10)
  actual = node.head.data
  assert actual == 10

def test_head_first_node():
    first_node = Linked_List()
    first_node.insert(18)
    excepted = 18
    actual = first_node.head.data
    assert excepted == actual


def test_multiple_nodes_insert():
    multiple = Linked_List()
    multiple.insert(5)
    multiple.insert(6)
    expected_head = 6
    expected_all_node= '6->5->NULL'
    actual_head = multiple.head.data
    actual_all_node = str(multiple)
    assert expected_head == actual_head
    assert expected_all_node == actual_all_node

def test_includes():
    include = Linked_List()
    include.insert(5)
    excepted = True
    actual = include.includes(5)
    assert excepted == actual

def test_not_includes():
    not_include = Linked_List()
    excepted = False
    actual = not_include.includes(5)
    assert excepted == actual

def test_collection():
    multiple = Linked_List()
    multiple.insert(5)
    multiple.insert(6)
    expected = '6->5->NULL'
    actual = str(multiple)
    assert expected == actual
