from stack_queue_brackets import __version__

from stack_queue_brackets.stack_queue_brackets import balance
def test_version():
    assert __version__ == '0.1.0'


def test_balanced_one():
    excepted = 'TRUE'
    actual = balance('()')
    assert excepted == actual

def test_balanced_tow():
    excepted = 'TRUE'
    actual = balance('([])')
    assert excepted == actual

def test_not_balanced_one():
    excepted = 'FALSE'
    actual = balance('])')
    assert excepted == actual

def test_not_balanced_tow():
    excepted = 'FALSE'
    actual = balance('[()])')
    assert excepted == actual
