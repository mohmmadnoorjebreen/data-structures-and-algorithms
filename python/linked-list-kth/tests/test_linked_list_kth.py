from linked_list_kth import __version__

from linked_list_kth.linked_list_kth import Node , LinkedList
def test_version():
    assert __version__ == '0.1.0'

def test_k_is_greater_than_the_length_of_the_linked_list():
    node = LinkedList()
    node.insert(1)
    node.insert(2)
    node.insert(3)
    try:
        node.kthFromEnd(10)
    except Exception as e:
        assert str(e) == "k is greater than the length of the linked list"

def test_k_and_the_length_of_the_list_are_the_same():
    node = LinkedList()
    node.insert(1)
    node.insert(2)
    node.insert(3)
    node.kthFromEnd(2)
    excepted = 3
    actual = node.head.data
    assert  excepted == actual

def test_k_is_not_a_positive_integer():
    node = LinkedList()
    node.insert(1)
    node.insert(2)
    try:
        node.kthFromEnd(-1)
    except Exception as e:
        assert str(e) == " k is not a positive integer"

def test_linked_list_is_of_a_size_1():
    node = LinkedList()
    node.insert(1)
    node.kthFromEnd(0)
    excepted = 1
    actual = node.head.data
    assert  excepted == actual


