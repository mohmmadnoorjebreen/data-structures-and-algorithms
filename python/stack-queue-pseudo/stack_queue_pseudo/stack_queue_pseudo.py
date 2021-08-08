class Node:

    def __init__(self,data=''):
        self.data= data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None


    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise Exception ( 'empty stack')

        temp = self.top
        self.top = self.top.next
        temp.next = None

        return temp.data

    def peek(self):
        if not self.top:
            raise Exception ( 'empty stack')

        return self.top.data

    def is_empty(self):
        return not self.top


    def __str__(self) -> str:
        string = ''
        temp = self.top

        while temp:
            string += f'{temp.data}->'
            temp = temp.next

        return string


class PseudoQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self,value):
        self.s1.push(value)

    def dequeue(self):
        if self.s2.top:
            value_remove =self.s2.pop()
        else:
            while self.s1.top:
                top = self.s1.pop()
                self.s2.push(top)
            value_remove =self.s2.pop()
        return value_remove


    def __str__(self) -> str:
        string = ''
        if self.s1.top:
            temp = self.s1.top
        else:
            temp = self.s2.top
        while temp:
            string += f'{temp.data}->'
            temp = temp.next

        return string


# if __name__ == '__main__':
#     x = PseudoQueue()
#     x.enqueue(10)
#     x.enqueue(15)
#     x.enqueue(20)
#     x.enqueue(5)

#     print(x)
#     print(x.dequeue())

#     print(x)

