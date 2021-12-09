from binarytree import Node

rootNode = Node(100)
rootNode.left = Node(3)
rootNode.left.left = Node(1)
rootNode.left.right = Node(6)
rootNode.left.right.right = Node(7)
rootNode.left.right.left = Node(4)
rootNode.right = Node(10)
rootNode.right.right = Node(14)
rootNode.right.right.right = Node(10)
rootNode.right.right.left = Node(13)

print(rootNode)

print("...................................................................................................")
print("Preorder Traversal : ",rootNode.preorder)
print("...................................................................................................")
print("Inorder Traversal : ",rootNode.inorder)
print("...................................................................................................")
print("Postorder Traversal : ",rootNode.postorder)
print("...................................................................................................")
