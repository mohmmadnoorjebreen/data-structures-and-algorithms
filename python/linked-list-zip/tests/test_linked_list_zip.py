from linked_list_zip import __version__

from linked_list_zip.linked_list_zip import zipLists , Linked_List

def test_version():
    assert __version__ == '0.1.0'


def test_zip_list_one_of_them_empty():
    first = Linked_List()
    first.insert(1)
    second = Linked_List()
    excepted = first
    actual = zipLists(first,second)
    assert excepted == actual

def test_zip_list_equal_of_len():
    first = Linked_List()
    first.insert(1)
    first.insert(2)
    second = Linked_List()
    second.insert(3)
    second.insert(4)
    excepted = '2->4->1->3->NULL'
    actual = str(zipLists(first,second))
    assert excepted == actual

def test_zip_list_when_the_first_list_longer():
    first = Linked_List()
    first.insert(1)
    first.insert(2)
    first.insert(3)
    second = Linked_List()
    second.insert(4)
    excepted = '3->4->2->1->NULL'
    actual = str(zipLists(first,second))
    assert excepted == actual

def test_zip_list_when_the_second_list_longer():
    first = Linked_List()
    first.insert(1)
    second = Linked_List()
    second.insert(2)
    second.insert(3)
    second.insert(4)
    excepted = '1->4->3->2->NULL'
    actual = str(zipLists(first,second))
    assert excepted == actual
