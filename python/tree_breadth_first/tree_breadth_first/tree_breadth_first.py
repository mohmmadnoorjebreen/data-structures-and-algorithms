class Node:

    def __init__(self,value=''):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None



def breadth_first(root):
        if root == None:
            raise Exception('no value')
        list_value = []
        crr = root
        data = []
        data.append(crr)

        while len(data) !=0:
            crr = data.pop(0)
            list_value.append(crr.value)

            if crr.left:
                data.append(crr.left)

            if crr.right :
                data.append(crr.right)

        return list_value






