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


def left_join(h1,h2):
    return_date =[]
    for value in h1._buckets:
        if value:
            for item in value:
                if h2.contains(item[0]):
                    h2_value = h2.get(item[0])
                    return_date.append([item[0],item[1],h2_value])
                else:
                    return_date.append([item[0],item[1],None])
    return return_date



