class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def check_loop(head):
    f=s=head
    while f and f.next:
        f=f.next.next
        s=s.next
        if f==s:
            print("loop")
            return
    print("No loop")
    return
def count_ofnode_loop(head):
    f = s = head
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            break
    else:
        print("No loop")
        return
    # Count the number of nodes in the loop
    count = 1
    temp = s.next
    while temp != s:
        count += 1
        temp = temp.next
    print("Count of elements in loop = ", count)
a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)
e=Node(50)
a.next=b
b.next=c
c.next=d
d.next=e
e.next=c
check_loop(a)
count_ofnode_loop(a)