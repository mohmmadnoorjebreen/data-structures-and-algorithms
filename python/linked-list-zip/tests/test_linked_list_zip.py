from linked_list_zip import __version__

from linked_list_zip.linked_list_zip import zipLists , Linked_List

def test_version():
    assert __version__ == '0.1.0'


def test_zip_list():
    y = Linked_List()
    y.insert(1)
    y.insert(2)
    y.insert(3)
    x = Linked_List()
    x.insert(4)
    x.insert(5)
    x.insert(6)
    excepted = 2
    actual = zipLists(x,y)
    assert excepted == actual
