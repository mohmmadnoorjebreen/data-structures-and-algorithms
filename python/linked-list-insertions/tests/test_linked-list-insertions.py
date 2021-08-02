from  linked_list_insertions.linked_list_insertions import Node , LinkedList



def test_add_node_to_end():
    node = LinkedList()
    node.insert(2)
    node.insert(5)
    node.append(10)
    excepted = '5->2->10->NULL'
    actual = str(node)
    assert actual == excepted

def test_add_multiple_node_to_end():
    node = LinkedList()
    node.insert(2)
    node.insert(5)
    node.append(10)
    node.append(11)
    excepted = '5->2->10->11->NULL'
    actual = str(node)
    assert actual == excepted

def test_insert_node_before_the_middle_node():
    node = LinkedList()
    node.insert(2)
    node.insert(5)
    node.append(10)
    node.append(11)
    node.insert_before(10,8)
    excepted = '5->2->8->10->11->NULL'
    actual = str(node)
    assert actual == excepted

def test_insert_node_before_the_first_node():
    node = LinkedList()
    node.insert(2)
    node.insert(5)
    node.append(10)
    node.append(11)
    node.insert_before(5,3)
    excepted = '3->5->2->10->11->NULL'
    actual = str(node)
    assert actual == excepted

def test_insert_node_after_the_middle_node():
    node = LinkedList()
    node.insert(2)
    node.insert(5)
    node.append(10)
    node.append(11)
    node.insert_after(2,4)
    excepted = '5->2->4->10->11->NULL'
    actual = str(node)
    assert actual == excepted

def test_insert_node_after_the_last_node():
    node = LinkedList()
    node.insert(2)
    node.insert(5)
    node.append(10)
    node.append(11)
    node.insert_after(11,20)
    excepted = '5->2->10->11->20->NULL'
    actual = str(node)
    assert actual == excepted

