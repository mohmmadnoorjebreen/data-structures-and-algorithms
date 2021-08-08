from stack_queue_pseudo import __version__

from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
def test_version():
    assert __version__ == '0.1.0'

def test_enqueue_when_empty():
    node = PseudoQueue()
    node.enqueue(10)
    excepted = 10
    actual = node.s1.top.data
    assert  excepted == actual

def test_enqueue():
    node = PseudoQueue()
    node.enqueue(10)
    node.enqueue(20)
    excepted = '20->10->'
    actual = str(node)
    assert  excepted == actual

def test_dequeue():
    node = PseudoQueue()
    node.enqueue(10)
    node.enqueue(20)
    node.dequeue()
    excepted = '20->'
    actual = str(node)
    assert  excepted == actual

