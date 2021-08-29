from blog import __version__

from blog.sort import InsertionSort

def test_version():
    assert __version__ == '0.1.0'

def test_sort():
    arr = [8, 4, 23, 42, 16, 15]
    InsertionSort(arr)
    excepted = [4, 8, 15, 16, 23, 42]
    actual = arr
    assert excepted == actual

def test_sort_Reverse_sorted():
    arr =[20, 18, 12, 8, 5, -2]
    InsertionSort(arr)
    excepted = [-2, 5, 8, 12, 18, 20]
    actual = arr
    assert excepted == actual

def test_sort_Few_uniques():
    arr = [5, 12, 7, 5, 5, 7]
    InsertionSort(arr)
    excepted = [5, 5, 5, 7, 7, 12]
    actual = arr
    assert excepted == actual

def test_sort():
    arr = [2, 3, 5, 7, 13, 11]
    InsertionSort(arr)
    excepted = [2, 3, 5, 7, 11, 13]
    actual = arr
    assert excepted == actual
