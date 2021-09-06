from .tree import BinaryTree , Node

class HashTable():


    def __init__(self,size = 50):
        self.size = size
        self._buckets = [None for _ in range(size)]


    def hash(self,key):
        """
        take a key as a string and
        return a index as int where value will set in bucket.
        """
        hash = 0
        key = str(key)
        for value in key :
            hash += ord(value)
        return (hash *3) % self.size

    def add(self,key,value):
        """
        add the value in index that takes from a key to bucket , no return.
        """
        index = self.hash(key)
        if not self._buckets[index] :
            self._buckets[index] = [[key,value]]
        else:
            self._buckets[index].append([key,value])

    def get(self,key):
        """
        return value that placed in index
        """
        index = self.hash(key)
        if not self._buckets[index] :
            raise Exception('no key like that')

        for value in self._buckets[index] :
            if value[0] == key:
                return value[1]


    def contains(self,key):
        """
        return if value in buckets or not
        """
        index = self.hash(key)
        if not self._buckets[index]:
            return False
        for value in self._buckets[index] :
            if value[0] == key:
                return True

    def tree_intersection(self,tree1,tree2):
        arr = []
        def helper(tree1):
            self.add(tree1.value,tree1.value)
            if tree1.left :
                helper(tree1.left)
            if tree1.right :
                helper(tree1.right)
        helper(tree1)
        def helper2(tree2):
            if self.contains(tree2.value):
               arr.append(tree2.value)
            if tree2.left :
                helper2(tree2.left)
            if tree2.right :
                helper2(tree2.right)
        helper2(tree2)
        return arr

