from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.intersection import HashTable
from hashmap_tree_intersection.tree import Node , BinaryTree

def test_version():
    assert __version__ == '0.1.0'


def test_tree_intersection():
    tree1 = BinaryTree()
    node = Node(10)
    tree1.root = node
    tree1.root.left=Node(4)
    tree1.root.left.left=Node(5)
    tree1.root.left.right=Node(8)
    tree1.root.right=Node(50)
    tree1.root.right.left=Node(30)

    tree2 = BinaryTree()
    node = Node(10)
    tree2.root = node
    tree2.root.left=Node(6)
    tree2.root.left.left=Node(8)
    tree2.root.left.right=Node(5)
    tree2.root.right=Node(0)
    tree2.root.right.left=Node(100)
    hash = HashTable()

    excepted = [10, 8, 5]
    actual = hash.tree_intersection(tree1.root,tree2.root)

    assert actual == excepted
