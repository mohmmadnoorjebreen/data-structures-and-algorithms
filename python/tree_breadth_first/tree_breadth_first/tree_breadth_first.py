class Node:

    def __init__(self,value=''):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.list_value = []


    def breadth_first(self):

        if self.root == None:
            raise Exception('no value')
        crr = self.root
        data = []
        data.append(crr)

        while len(data) !=0:
            crr = data.pop(0)
            self.list_value.append(crr.value)

            if crr.left:
                data.append(crr.left)

            if crr.right :
                data.append(crr.right)

        return self.list_value






