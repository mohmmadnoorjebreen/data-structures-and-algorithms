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


    def __str__(self) -> str:
        string = ''
        temp = self.top

        while temp:
            string += f'{temp.data}->'
            temp = temp.next

        return string

class AnimalShelter:
        def __init__(self):
            self.s_cat1 = Stack()
            self.s_cat2 = Stack()
            self.s_dog1 = Stack()
            self.s_dog2 = Stack()

        def enqueue(self,animal):
            if animal.pref == 'cat':
                self.s_cat1.push(animal.name)
            elif animal.pref == 'dog':
                self.s_dog1.push(animal.name)
            else:
                return 'null'


        def dequeue(self,pref):
            if pref == 'cat':
                if self.s_cat2.top:
                    value_remove =self.s_cat2.pop()
                else:
                    while self.s_cat1.top:
                        top = self.s_cat1.pop()
                        self.s_cat2.push(top)
                    value_remove =self.s_cat2.pop()
                return value_remove
            elif pref == 'dog':
                if self.s_dog2.top:
                    value_remove =self.s_dog2.pop()
                else:
                    while self.s_dog1.top:
                        top = self.s_dog1.pop()
                        self.s_dog2.push(top)
                    value_remove =self.s_dog2.pop()
                return value_remove
            else :
                return 'null'

        def __str__(self) -> str:
                string = ''
                if self.s_cat1.top:
                    temp = self.s_cat1.top
                else:
                    temp = self.s_cat2.top
                while temp:
                    string += f'{temp.data}->'
                    temp = temp.next
                return string




class Dogs:

    def __init__(self,name=''):
        self.name = name
        self.pref = 'dog'

class Cats:
    def __init__(self,name=''):
        self.name = name
        self.pref = 'cat'

class Bird:
    def __init__(self,name=''):
        self.name = name
        self.pref = 'bird'





if __name__ == '__main__':
    print('work')
    x = Cats('maia')
    y = AnimalShelter()
    y.enqueue(x)
    print(y)

