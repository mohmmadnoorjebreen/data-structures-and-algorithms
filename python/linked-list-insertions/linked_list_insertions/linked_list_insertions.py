


class Node:

    def __init__(self,data =''):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self , value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def append(self,value):
        node = Node(value)
        currants = self.head
        while currants:
            if currants.next != None:
                currants = currants.next
            else:
                currants.next = node
                break

    def insert_after(self,num,value):
        node = Node(value)
        currants = self.head
        while currants:
            if currants.data == num:
                node.next = currants.next
                currants.next = node
                break
            else:
                currants = currants.next

    def insert_before(self,num,value):
        node = Node(value)
        currants = self.head
        if currants.data == num:
            node.next = currants
            self.head= node
            return 'done'

        while currants:
            if currants.next.data == num:
                node.next = currants.next
                currants.next = node
                break
            else:
                currants = currants.next

    def __str__(self):
        string = ''
        currants = self.head
        while currants:
            string += f'{str(currants.data)}->'
            currants = currants.next
        string += 'NULL'
        return string


# print('work')
# x = LinkedList()
# x.insert(4)
# x.append(3)
# x.append(5)
# # x.insert_after(5,4)
# x.insert_before(5,1)
# print(x)

