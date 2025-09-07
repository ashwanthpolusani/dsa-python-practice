class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def insert(self,data,root):
        if root==None:
            newnode=Node(data)
            root=newnode
            return
        if data>root.data:
            self.insert(data,root.right)
        else:
            self.insert(data,root.left)


    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    
    def preorder(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
    
    def sum_all(self,root):
        return 0 if root==None else root.data+self.sum_all(root.left) + self.sum_all(root.right)
    
    def sum_even(self,root):
        if root==None:
            return 0
        return self.sum_even(root.left) + self.sum_even(root.right) + (root.data if root.data%2==0 else 0) 
    def height_tree(self,root):
        if root==None:
            return -1
        return max(self.height_tree(root.left),self.height_tree(root.right))+1
    
    def search(self,ele,root):
        if root==None:
            return False
        if root.data==ele:
            return True
        return self.search(ele,root.left) if root.data>ele  else self.search(ele,root.right)
    
    def count_leafNodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.count_leafNodes(root.left)+self.count_leafNodes(root.right)

    def all_path(self,root,path=[]):
        if root==None:
            return 
        path.append(root.data)
        if root.left==None and root.right==None:
            print(path)
            path.pop()
            return
        self.all_path(root.left,path) 
        self.all_path(root.right,path)
        path.pop()

    def bfs(self,root):
        q=[root]
        c=1
        while q:
            r=q.pop(0)
            print(r.data)
            if r.left:
                q.append(r.left)
                c+=1
            if r.right:
                q.append(r.right)
                c+=1
        print(f"Count of nodes ={c}")

    def left_view(self,root,c=0,d={}):
        if root==None:
            return
        if c not in d:
            d[c]=root.data
        self.left_view(root.left,c+1)
        self.left_view(root.right,c+1)
        return d
    
    def right_view(self,root,c=0,d={}):
        if root==None:
            return
        if c not in d:
            d[c]=root.data
       
        self.right_view(root.right,c+1)
        self.right_view(root.left,c+1)
        return d
    
    def top_view(self,root,d={}):
        if root==None:
            return
        q=[(root,0)]
        while q:
            r=q.pop()
            if r[-1] not in d:
                d[r[-1]]=r[0].data
            if r[0].left:
                q.append((r[0].left,r[-1]-1))
            if r[0].right:
                q.append((r[0].right,r[-1]+1))
        return d
    
    def bottom_view(self,root,d={}):
        if root==None:
            return
        q=[(root,0)]
        while q:
            r=q.pop()
            d[r[-1]]=r[0].data
            if r[0].left:
                q.append((r[0].left,r[-1]-1))
            if r[0].right:
                q.append((r[0].right,r[-1]+1))
        return d
    
    def lca_bt(self,root,a,b):
        if root==None:
            return 
        if root.data==a or root.data==b:
            return root
        l=self.lca_bt(root.left,a,b)
        r=self.lca_bt(root.right,a,b)
        if l!=None and r!=None:
            return root.data
        if l!=None:
            return l
        else:
            return r
    
    def low_comm_ancestor_bst(self,root,a,b):
        if root==None:
            return
        if root.data<a and root.data<b:
            return self.low_comm_ancestor_bst(root.right,a,b)
        elif root.data>a and root.data>b:
            return self.low_comm_ancestor_bst(root.left,a,b)
        else:
            return root.data
        
    def tree_balanced(self,root):
        bal=True
        def check(root):
            if root==None:
                return -1
            l=check(root.left)
            r=check(root.right)
            if l-r>1 or l-r<-1:
                bal=False
            return l-r
        check(root)
        return "Balanced" if bal else "Not Bal" 



r=Node(10)
r.left=Node(5)
r.right=Node(20)
r.left.left=Node(2)
r.left.right=Node(8)
r.left.right.left=Node(7)
r.left.right.right=Node(9)
# r.right.left=Node(15)
# r.right.right=Node(22)
t=Tree()
# t.preorder(r)
# print()
# t.postorder(r)
# print()
# t.inorder(r)
# print()
# print(t.sum_all(r))
# print(t.sum_even(r))
# print(t.height_tree(r))
# print(t.search(90,r))
# print(t.count_leafNodes(r))
# t.all_path(r)
# t.bfs(r)
# print(t.left_view(r))
# print(t.right_view(r))
# print(t.top_view(r))
# print(t.bottom_view(r))
# print(t.low_comm_ancestor_bst(r,2,9))
# print(t.lca_bt(r,2,9))
print(t.tree_balanced(r))