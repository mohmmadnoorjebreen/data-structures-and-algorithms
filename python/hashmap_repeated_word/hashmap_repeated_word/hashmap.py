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

    def hashmap_repeated_word(self,str):
        """
        return first repetend word  in str as string
        """
        arr1 = str.split(',')
        arr2 = ' '.join(arr1)
        arr = arr2.split()
        for value in arr:
            values = value.lower()
            if self.contains(values):
                return value
            else:
                self.add(values,value)





