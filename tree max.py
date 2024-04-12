class newNode:
     def __init__(self,data):
         self.data=data
         self.left=self.right = None
         def findMax(root):
             if(root==None):
                 return float('-inf')
             child = root.data
             lchild = findMax(root.left)
             rchild =findMax(root.right)
             if (lchild > child):
                 child = lchild
                 if (rchild > child):
                     child = rchild
                     return child 
                 lchild = findMax(root.left)
                 rchild = findMax(root.right)
                 if (lchild > child):
                     child = lchild
                 if (rchild > child):
                   child = rchild
                   return child
         if __name__=='__main__':
          root=newNode(3)
          root.left=newNode(7)
          root.right = newNode(6)
          root.left.right = newNode(8)
          root.left.right.left = newNode(1)
          root.left.right.right = newNode(15)
          root.right.right = newNode(9)
          root.right.right.left = newNode(4)
          print("Maximum",
         findMax(root))










