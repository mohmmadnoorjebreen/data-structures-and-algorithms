from trees import __version__
from trees.trees import BinaryTree, BinarySearchTree

def test_version():
    assert __version__ == '0.1.0'



def test_instantiate_an_empty_tree():
    tree = BinarySearchTree()
    excepted = None
    actual = tree.root
    assert excepted == actual

def test_instantiate_a_tree_with_a_single_root_node():
    tree = BinarySearchTree()
    tree.add(6)
    excepted = 6
    actual = tree.root.value
    assert excepted == actual

def test_add_a_left_child_and_right_child_to_a_single_root_node():
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(10)
    tree.add(5)
    excepted_left = 5
    excepted_right = 10
    actual_left = tree.root.left.value
    actual_right = tree.root.right.value
    assert actual_left == excepted_left and actual_right == excepted_right


def test_return_a_collection_from_a_pre_order_traversal():
    tree = BinarySearchTree()
    tree.insert(6)
    tree.insert(5)
    tree.insert(10)
    excepted = '6>5>10>'
    actual = tree.pre_order(tree.root)
    assert excepted == actual

def test_return_a_collection_from_an_in_order_traversal():
    tree = BinarySearchTree()
    tree.insert(6)
    tree.insert(5)
    tree.insert(10)
    excepted = '5>6>10>'
    actual = tree.in_order(tree.root)
    assert excepted == actual


def test_return_a_collection_from_a_post_order_traversal():
    tree = BinarySearchTree()
    tree.insert(6)
    tree.insert(5)
    tree.insert(10)
    excepted = '5>10>6>'
    actual = tree.post_order(tree.root)
    assert excepted == actual
