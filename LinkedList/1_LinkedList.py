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

    def sum_of_nodes(self):
        temp=self.head
        sum=0
        while temp!=None:
            sum+=temp.data
            temp=temp.next
        print(f"Sum of all Nodes = {sum}")
    
    def sum_even_numbers(self):
        temp = self.head
        even_sum = 0
        while temp is not None:
            if temp.data % 2 == 0:
                even_sum += temp.data
            temp = temp.next
        print("Even sum = ", even_sum)
    
    def sum_Of_even_pos(self):
        temp = self.head
        pos = 1
        even_sum = 0
        while temp is not None:
            if pos % 2 == 0:
                even_sum += temp.data
            temp = temp.next
            pos += 1
        print("Even positions sum = ", even_sum)

    def second_largest(self):
        temp=self.head
        m1=m2=-float('inf')
        while temp:
            if temp.data>m1:
                m2=m1
                m1=temp.data
            if temp.data>m2 and temp.data<m1:
                m2=temp.data
            temp=temp.next
        print(f"Second Largest Element = {m2}")
    
    # returns a count of conscetuive elements whose sum is <= k
    def consecutive_pair(self,k):
        count=0
        temp=self.head
        while temp.next:
            if temp.next.data+temp.data<=k:
                count+=1
            temp=temp.next
        print(f"Count of pairs less than or equal to {k} are : {count}")

    def all_possible_ksum_pairs(self,k):
        count=0
        temp=self.head
        while temp.next:
            temp1=temp.next
            if temp.data>k: # Assuming we have only whole numbers (0-"infinity") in the linked
                temp=temp.next
                continue
            while temp1:
                if temp1.data+temp.data<=k:
                    count+=1
                temp1=temp1.next
            temp=temp.next
        print(f"Count of all pairs whose sum <= {k} = {count}")
    
    # Using heir - tortoise Algorithm
    def second_half(self):
        temp=self.head
        half=self.head
        while temp and temp.next: 
            half=half.next
            temp=temp.next.next
        while half:
            print(half.data,end="->")
            half=half.next
        print(None)

    def mid(self):
        fast=slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        print(f"Mid = {slow.data}")

    def kth_node_from_last(self,k):
        c=k
        fast=self.head
        slow=self.head
        while fast:
            if k==0:
                slow=slow.next
            else:
                k-=1
            fast=fast.next
        print(f"Node {c} from last is {slow.data}")

    def remove_kth_last_element(self,k):
        if not self.head:  # Check if the list is empty
            return
        slow=fast=self.head
        count = 0
        while fast:
            if count >= k:
                slow = slow.next
            fast = fast.next
            count += 1
        if count < k:  # If k is larger than the length of the list
            return
        if slow == self.head and k == count:  # If kth last element is the head
            self.head = self.head.next
        elif slow.next:  # Normal case
            slow.next = slow.next.next
        else:  # If there is only one element in the list and k is 0
            self.head = None
        self.display()

    def swap_consecutive_ele(self):
        temp=self.head
        while temp and temp.next:
            temp.data,temp.next.data=temp.next.data,temp.data
            temp=temp.next.next
        self.display()

    def bubble_sort(self):
        t=self.head
        while t:
            flag=True
            t1=self.head
            t2=t.next
            while t2:
                if t1.data>t1.next.data:
                    t1.data,t1.next.data=t1.next.data,t1.data
                    flag=False
                t1=t1.next
                t2=t2.next
            if flag:
                break
            t=t.next
        self.display()

    def kth_largest_element(self,k):
        t=self.head
        c=0
        while t and c<k:
            t1=self.head
            t2=t.next
            while t2:
                if t1.data>t1.next.data:
                    t1.data,t1.next.data=t1.next.data,t1.data
                t1=t1.next
                t2=t2.next
            t=t.next
            c+=1
        print(t1.data)

    def insert_element(self,val):
        new_node=Node(val)
        if self.head==None :
            self.head=new_node
            return
        if self.head.data>val:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            if temp.data<val and temp.next.data>val:
                break
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node

    def check_loop(self):
        f=s=self.head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                print("loop")
                return
        print("No loop")
        return 

 
        

a=Linked()
l=[10,92,23,20,30,40,89]
l.sort(reverse=True)
for i in l:
    a.insert(i)

# a.sum_of_nodes()
# a.display()
# a.sum_Of_even_pos()
# a.second_largest()
# a.consecutive_pair(90)
# a.all_possible_ksum_pairs(90)
# a.second_half()
# a.mid()
# a.kth_node_from_last(2)
# a.remove_kth_last_element(2)
# a.swap_consecutive_ele()
# a.bubble_sort()
# a.kth_largest_element(4)
# a.insert_element(7)
a.check_loop()
# a.display()


