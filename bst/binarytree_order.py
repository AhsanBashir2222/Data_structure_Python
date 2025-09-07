class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# pre_order


def preorder(node):
    if node is None:
        return
    print(node.data, end="->")
    preorder(node.left)
    preorder(node.right)

# inorder


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end="->")
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end="->")


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
# traverse
preorder(root)
print("\n")
inorder(root)
print("\n")
postorder(root)
