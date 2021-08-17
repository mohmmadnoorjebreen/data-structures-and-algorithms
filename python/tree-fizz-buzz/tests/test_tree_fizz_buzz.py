from tree_fizz_buzz import __version__

from tree_fizz_buzz.test_tree_fizz_buzz import fizz_buzz_tree , KTree , Node
def test_version():
    assert __version__ == '0.1.0'


def test_If_the_value_is_divisible_by_3_replace_the_value_with_Fizz():
    tree= KTree()
    tree.root = Node(3)
    excepted = 'Fizz'
    actual = fizz_buzz_tree(tree.root).value
    assert excepted == actual

def test_If_the_value_is_divisible_by_5_replace_the_value_with_Buz():
    tree= KTree()
    tree.root = Node(3)
    tree.root.children.append(Node(5))
    excepted = 'Buzz'
    actual = fizz_buzz_tree(tree.root).children[0].value
    assert excepted == actual

def test_If_the_value_is_divisible_by_3_and_5_replace_the_value_with_FizzBuzz():
    tree= KTree()
    tree.root = Node(3)
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(15))
    excepted = 'FizzBuzz'
    actual = fizz_buzz_tree(tree.root).children[1].value
    assert excepted == actual

def test_If_the_value_is_not_divisible_by_3_or_5_simply_turn_the_number_into_a_String():
    tree= KTree()
    tree.root = Node(3)
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(2))
    excepted = '2'
    actual = fizz_buzz_tree(tree.root).children[1].value
    assert excepted == actual
