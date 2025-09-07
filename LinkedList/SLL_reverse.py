class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def reverse(self):
        prev=None
        temp=self.head
        next=None
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev

    def reverse_half(self):
        f=s=self.head
        while f and f.next and f.next.next:
            s=s.next
            f=f.next.next
        prev=next=None
        temp=s.next
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        print(s.data)
        s.next=prev

a=Linked()
l=[10,92,23,11,56]
l.sort(reverse=True)
for i in l:
    a.insert(i)
a.display()
a.reverse()
a.display()
a.reverse_half()
a.display()