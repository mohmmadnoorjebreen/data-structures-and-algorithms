class Node:

    def __init__(self,data=''):
        self.data= data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node = Node(value)

        if not self.front:
            self.front = node
            self.front.next = self.rear
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            raise Exception ('empty queue')

        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.data

    def peek(self):
        if not self.front:
            raise Exception ( 'empty queue')

        return self.front.data

    def is_empty(self):
        return not self.front

    def __str__(self) -> str:
        string = ''
        temp = self.front

        while temp:
            string += f'{temp.data}->'
            temp = temp.next

        return string
