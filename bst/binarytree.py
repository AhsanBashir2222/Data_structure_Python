class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


root = TreeNode("root")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("root.left", root.left.data)
print("root.right", root.right.data)
print("nodeA.left ", nodeA.left.data)
print("nodeA.right", root.left.right.data)
print("nodeB.left", nodeB.left.data)
print("nodeB.right", root.right.right.data)
print("findE", root.right.left.data)
