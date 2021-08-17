class Node:

    def __init__(self,value=''):
        self.value = value
        self.children = []



class KTree:

    def __init__(self):
        self.root = None



def fizz_buzz_tree(root):
        if root == None:
            return root
        crr = root
        data = []
        data.append(crr)

        while len(data) !=0:
            crr = data.pop(0)
            if crr.value % 15==0:
                crr.value = 'FizzBuzz'
            elif crr.value % 5 == 0:
                crr.value = 'Buzz'
            elif crr.value % 3 == 0:
                crr.value = 'Fizz'
            else:
                crr.value = str(crr.value)

            for node in crr.children:
                data.append(node)
        return root


if __name__ == '__main__':
    print('good')
    tree= KTree()
    tree.root = Node(11)
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(7))
    tree.root.children.append(Node(2))
    tree.root.children.append(Node(6))
    tree.root.children[0].children.append(Node(5))
    tree.root.children[0].children.append(Node(5))
    tree.root.children[1].children.append(Node(0))
    print(fizz_buzz_tree(tree.root).children[1].value)


