from tree import Node, BinaryTree

def tree_intersection(tree1, tree2):
    listTree = []
    def walk(root1, root2):
        if not root1:
            return
        current1 = root1.value
        current2 = root2.value
        if current1 == current2:
            listTree.append(current1)
        walk(root1.left, root2.left)
        walk(root1.right, root2.right)

    walk(tree1.root, tree2.root)
    return listTree

