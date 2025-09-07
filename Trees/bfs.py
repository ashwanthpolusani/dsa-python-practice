class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
a=Tree()
a.insert(15)
a.insert(10)
a.insert(20)
a.insert(5)
a.insert(7)
a.insert(22)
r=a.insert(17)
a.inorder(r)