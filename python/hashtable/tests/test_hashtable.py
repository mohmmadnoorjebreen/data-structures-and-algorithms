from hashtable import __version__
from hashtable.hashtable import HashTable

def test_version():
    assert __version__ == '0.1.0'



def test_add_and_get_hashtable():
    hash = HashTable()
    hash.add('mohammad',15156)
    excepted = 15156
    actual = hash.get('mohammad')
    assert excepted == actual


def test_Successfully_returns_null_for_a_key_that_does_not_exist_in_the_hashtable():
    hash = HashTable()
    excepted = False
    actual = hash.contains('mohammad')
    assert excepted == actual


def test_Successfully_handle_a_collision_within_the_hashtable():
    hash = HashTable()
    index = hash.hash('abc')
    hash.add('abc',20)
    hash.add('cba',40)
    excepted = 2
    actual = len(hash._buckets[index])
    assert actual == excepted


def test_Successfully_retrieve_a_value_from_a_bucket_within_the_hashtable_that_has_a_collision():
    hash = HashTable()
    hash.add('abc',20)
    hash.add('cba',40)
    excepted_abc = 20
    excepted_cba = 40
    actual_abc = hash.get('abc')
    actual_cba = hash.get('cba')
    assert excepted_abc == actual_abc
    assert excepted_cba == actual_cba

def test_Successfully_hash_a_key_to_an_in_range_value():
    hash = HashTable()
    index=hash.hash('abc')
    expected = True
    actual = index in range(50)
    assert expected == actual

