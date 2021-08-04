class Node:
    def __init__(self,data=''):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None

    def insert(self,data):
        node = Node(data)
        if self.head:
            node.next = self.head

        self.head = node

    def kthFromEnd(self,value):
        if value < 0:
            raise Exception(' k is not a positive integer')
        value+=1
        len = 0
        currants = self.head
        while currants:
            len += 1
            currants = currants.next
        if value > len:
            raise Exception("k is greater than the length of the linked list")
        else:
            currants = self.head
            for data in range(len-value):
                currants = currants.next

        return currants.data


    def __str__(self):

        string = ''
        currants = self.head

        while currants:
            string += f'{str(currants.data)}->'
            currants = currants.next
        string += 'NULL'
        return string


x = LinkedList()
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)
print(x)
print(x.kthFromEnd(0))
