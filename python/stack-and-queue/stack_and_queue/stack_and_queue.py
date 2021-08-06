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



if __name__ == '__main__':
    print('work')
    # x = Stack()
    # print('should be true',x.is_empty())
    # x.push(1)
    # print('should be false',x.is_empty())
    # x.push(2)
    # print('peek before pop' , x.peek())
    # print('all push',x)
    # print('pop top',x.pop())
    # print('push after pop',x)
    # print('peek after pop' , x.peek())
    x= Queue()
    print('is empty should be true',x.is_empty())
    x.enqueue(1)
    print(x)
    print('is empty should be false',x.is_empty())
    print('peek 1',x.peek())
    x.enqueue(2)
    print(x)
    print('peek 1',x.peek())
    x.enqueue(3)
    print('peek 1',x.peek())
    print(x)
    print('it should 1 =>',x.dequeue())
    print(x)
    print('peek 2',x.peek())


