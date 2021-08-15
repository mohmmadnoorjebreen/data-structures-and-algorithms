from tree_max import __version__

from tree_max.tree_max import BinaryTree , Node
def test_version():
    assert __version__ == '0.1.0'



def test_max_num_when_empty_tree():
    tree = BinaryTree()
    try :
        tree.max_num()
    except Exception as e:
        assert str(e) == 'empty tree'



def test_max_num():
    tree = BinaryTree()
    tree.root = Node(20)
    tree.root.right = Node(50)
    tree.root.left = Node(70)
    tree.root.left.left = Node(22)
    tree.root.left.right = Node(66)
    excepted = 70
    actual = tree.max_num()
    assert excepted == actual
