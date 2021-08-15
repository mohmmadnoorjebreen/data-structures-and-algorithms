
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
        max_num =[]
        while len(data) !=0:
            crr = data.pop()

            if crr.left:
                data.append(crr.left)
                max_num.append(crr.left.value)

            if crr.right :
                data.append(crr.right)
                max_num.append(crr.right.value)

        return max(max_num)




if __name__ == '__main__':
    print('good')
    x = BinaryTree()
    x.insert(111)
    x.insert(666)
    x.insert(10000)
    print(x.max_num())

