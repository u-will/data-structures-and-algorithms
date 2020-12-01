class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        # root, left, right
        values = []
        def walk(position):
            if not position:
                return
            values.append(position.value)
            walk(position.left)
            walk(position.right)
        walk(self.root)
        return values

    def in_order(self):
        # left, root, right
        values = []
        def walk(position):
            if not position:
                return
            walk(position.left)
            values.append(position.value)
            walk(position.right)
        walk(self.root)
        return values

    def post_order(self):
        # left, right, root
        values = []
        def walk(position):
            if not position:
                return
            walk(position.left)
            walk(position.right)
            values.append(position.value)
        walk(self.root)
        return values

class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_n = Node(value)

        def configure(position, new):
            if not position:
                return
            if new_n.value < position.value:
                if not position.left:
                    position.left = new_n
                else:
                    configure(position.left, new_n)
            else:
                if not position.right:
                    position.right = new_n
                else:
                    configure(position.right, new_n)
        if not self.root:
            self.root = new_n
            return self.root
        configure(self.root, new_n)

    def contains(self, value):
        if values not in self.pre_order():
            return False
        else:
            return True

tree_stuff = BinarySearchTree()
tree_stuff.add(2)
tree_stuff.add(7)
tree_stuff.add(5)
tree_stuff.add(10)
tree_stuff.add(0)
tree_stuff.pre_order()
