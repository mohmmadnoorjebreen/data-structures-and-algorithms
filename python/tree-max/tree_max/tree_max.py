
class Node:

    def __init__(self,value=''):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.max = 0

    def insert(self,value):
        node = Node(value)
        if not self.root:
            self.root = node

        elif not self.root.left:
            self.root.left = node

        elif not self.root.right:
            self.root.right = node

    def max_num(self):

        if self.root == None:
            raise Exception('empty tree')
        crr = self.root
        data = []
        data.append(crr)
        self.max = self.root.value
        while len(data) !=0:
            crr = data.pop()

            if crr.left:
                data.append(crr.left)
                if crr.left.value > self.max:
                    self.max = crr.left.value


            if crr.right :
                data.append(crr.right)
                if crr.right.value > self.max:
                    self.max = crr.right.value

        return self.max




if __name__ == '__main__':
    print('good')
    x = BinaryTree()
    x.insert(1111111111111)
    x.insert(444444444444444)
    x.insert(4233333333333333)
    print(x.max_num())

