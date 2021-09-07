from hashmap_left_join import __version__

from hashmap_left_join.hash_join import HashTable , left_join
def test_version():
    assert __version__ == '0.1.0'


def test_joined_one():
    hash1 = HashTable()
    hash1.add('good','fine')

    hash2 = HashTable()
    hash2.add('good','bad')

    expected = [['good', 'fine', 'bad']]
    actual = left_join(hash1, hash2)

    assert actual == expected

def test_joined_two():
    hash1 = HashTable()
    hash1.add('good','fine')

    hash2 = HashTable()
    hash2.add('yes','no')

    expected = [['good', 'fine', None]]
    actual = left_join(hash1, hash2)

    assert actual == expected
