class TreeNode:
 def __init__(self,data):
  
  self.data = data
  self.left =None
  self.right=None

root = TreeNode(10)
root.left = TreeNode(40)
left__child__data = root.left.data
print( left__child__data)
root=TreeNode(30)
root.right=TreeNode(50)
right__child__data =root.right.data
print(right__child__data)






