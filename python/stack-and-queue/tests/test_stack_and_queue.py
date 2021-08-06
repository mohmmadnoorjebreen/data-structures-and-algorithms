from stack_and_queue import __version__

import pytest

from stack_and_queue.stack_and_queue import Stack , Queue
def test_version():
    assert __version__ == '0.1.0'


def test_push_onto_a_stack():
    node = Stack()
    node.push(1)
    excepted =1
    actual = node.top.data
    assert excepted == actual

def test_push_multiple_values_onto_a_stack():
    node = Stack()
    node.push(1)
    node.push(2)
    excepted =2
    actual = node.top.data
    assert excepted == actual

def test_pop_off_the_stack():
    node = Stack()
    node.push(1)
    node.push(2)
    node.pop()
    excepted =1
    actual = node.top.data
    assert excepted == actual

def test_empty_a_stack_after_multiple_pops():
    node = Stack()
    node.push(1)
    node.push(2)
    node.pop()
    node.pop()
    excepted =True
    actual = node.is_empty()
    assert excepted == actual

def test_peek_the_next_item_on_the_stack():
    node = Stack()
    node.push(1)
    node.push(2)
    excepted =2
    actual = node.peek()
    assert excepted == actual

def test_instantiate_an_empty_stack():
    node = Stack()
    assert node.is_empty()

def test_Calling_pop_or_peek_on_empty_stack_raises_exception():
    node = Stack()
    try:
        node.pop()
    except Exception as e:
        assert str(e) == "empty stack"

def test_enqueue_into_a_queue():
    node = Queue()
    node.enqueue(1)
    excepted =1 , 1
    actual = node.rear.data , node.front.data
    assert excepted == actual

def test_enqueue_multiple_values_into_a_queue():
    node = Queue()
    node.enqueue(1)
    node.enqueue(2)
    excepted =2 , 1
    actual = node.rear.data , node.front.data
    assert excepted == actual

def test_dequeue_out_of_a_queue_the_expected_value():
    node = Queue()
    node.enqueue(1)
    node.enqueue(2)
    excepted =1
    actual = node.dequeue()
    assert excepted == actual

def test_peek_into_a_queue_seeing_the_expected_value():
    node = Queue()
    node.enqueue(2)
    excepted =2
    actual = node.peek()
    assert excepted == actual

def test_empty_a_queue_after_multiple_dequeues():
    node = Queue()
    node.enqueue(1)
    node.enqueue(2)
    node.dequeue()
    node.dequeue()
    excepted = True
    actual = node.is_empty()
    assert excepted == actual


def test_instantiate_an_empty_queue():
    node = Queue()
    assert node.is_empty()

def test_Calling_dequeue_or_peek_on_empty_queue_raises_exception():
    node = Queue()
    try:
        node.peek()
    except Exception as e:
        assert str(e) == 'empty queue'


