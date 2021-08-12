


class Node:

    def __init__(self,value=''):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.string_post = ''
        self.string_in = ''
        self.string_pre = ''

    def insert(self,value):
        node = Node(value)
        if not self.root:
            self.root = node

        elif not self.root.left:
            self.root.left = node

        elif not self.root.right:
            self.root.right = node

    def pre_order(self,root):


        self.string_pre += f'{root.value}>'

        if root.left:
            self.pre_order(root.left)

        if root.right:
            self.pre_order(root.right)
        return self.string_pre

    def in_order(self,root):

        if root.left:
            self.in_order(root.left)


        self.string_in += f'{root.value}>'

        if root.right:
            self.in_order(root.right)
        return self.string_in

    def post_order(self,root):

        if root.left:
            self.post_order(root.left)

        if root.right:
            self.post_order(root.right)


        self.string_post += f'{root.value}>'
        return self.string_post



class BinarySearchTree(BinaryTree):


    def add(self,value):
        node = Node(value)
        if not self.root:
            self.root = node
            return 'done'
        crr = self.root
        while True:
            if crr.value == value:
                return
            if crr.value> value:
                if crr.left:
                    crr = crr.left
                elif not crr.left:
                    crr.left = node
                    break
            elif crr.value < value:
                if crr.right:
                    crr = crr.right
                elif not crr.right:
                    crr.right = node
                    break


                
    def contains(self,value):
        if not self.root:
            raise Exception('empty tree')
        crr = self.root
        while True:

            if crr.value == value:
                return True
            elif crr.value> value:
                if crr.left:
                    crr = crr.left
                elif not crr.left:
                    return False
            elif crr.value < value:
                if crr.right:
                    crr = crr.right
                elif not crr.right:
                    return False






















