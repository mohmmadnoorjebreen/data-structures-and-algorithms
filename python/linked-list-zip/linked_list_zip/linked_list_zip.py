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

def zipLists(l1,l2):
    first = l1.head
    second = l2.head

    if not first :
      return l2
    if not second :
      return l1

    while first and second:
        if second:
            save_first = first.next
            first.next = second
            first = save_first
        if first:
            save_second = second.next
            second.next = first
            second = save_second

    return l1




if __name__ == '__main__':
    # x = Linked_List()
    # x.insert(1)
    # x.insert(2)
    # x.insert(3)
    # x.insert(4)

    # y = Linked_List()

    # y.insert(5)
    # # y.insert(6)
    # # y.insert(7)
    # # print(x)
    # # print(y)
    # # print(zipLists(x,y))
    # d = Linked_List()
    # d.insert(0)
    # d.insert(1)
    # d.insert(2)
    # d.insert(3)
    # c = Linked_List()
    # c.insert(4)
    # c.insert(5)
    # print(zipLists(d,c))
    print('work')

