import math
def convert_to_binary(num):
    def bin(a,n,s=""):
        if a==-1:
            return a
        if len(s)==n:
            print(s)
            a=a-1
            return a
        a=bin(a,n,s+'0')
        a=bin(a,n,s+'1')
        return a
    n=int(math.log(num,2))+1
    bin(num,n)

n=int(input("Enter the number: "))
print(convert_to_binary(n))
