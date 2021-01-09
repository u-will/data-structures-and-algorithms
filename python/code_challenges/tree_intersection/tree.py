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

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def walk(root):
            if value < root.value:
                if not root.left:
                    root.left = Node(value)
                else:
                    walk(root.left)
            else:
                if not root.right:
                    root.right = Node(value)
                else:
                    walk(root.right)

        walk(self.root)
