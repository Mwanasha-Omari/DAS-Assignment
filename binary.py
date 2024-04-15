class TreeNode:
 def __init__(self,data):
  self.data = data
  self.left =None
  self.right=None

def inorderTraversal(root):
    if root:
      
     inorderTraversal(root.left)
     print(root.data)
     inorderTraversal(root.right)

root = TreeNode(12)
root.left = TreeNode(5)
root.right= TreeNode(13)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(11)
  

print("inorderTraversal:")
inorderTraversal(root)













