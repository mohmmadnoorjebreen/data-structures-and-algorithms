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


    def __str__(self):

        string = ''
        currants = self.head

        while currants:
            string += f'{str(currants.data)}->'
            currants = currants.next
        string += 'NULL'
        return string

def zipLists(x,y):
    currants_x = x.head
    currants_y = y.head

    while currants_y :
        currants_x.next.next = currants_y.next
        currants_y.next = currants_x.next
        currants_x.next = currants_y
        break

    return currants_x.next.next.next.data





