class Node:
    def __init__(self,data=''):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head= None

    def insert(self,data):
        node = Node(data)
        if self.head:
            node.next = self.head

        self.head = node

    def includes(self,data):
        for value in self.iterate_item():
           if value == data:
                return True
        return False

    def iterate_item(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
            
    def __str__(self):

        string = ''
        currants = self.head

        while currants:
            string += f'{str(currants.data)}->'
            currants = currants.next
        string += 'NULL'
        return string


# if __name__ == '__main__':
#     print('work')
#     x = Linked_List()
#     x.insert(7)
#     x.insert(9)
#     x.insert(10)
#     print(x)
#     print(x.includes(10))
#     print(x.head.next)




