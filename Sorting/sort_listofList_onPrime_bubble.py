# Sorts a list of lists a using the bubble sort algorithm based on the single prime number in each list.
# The prime number in the sublist is at different indices
# Each sublist has 3 element, anyone element is definitely prime


def findprime(a):
    pl=[]
    for l in a:
        for n in l:
            for i in range(2,int(n**(0.5))+1):
                if n%i==0:
                    break
            else:
                pl.append(n)
    return pl

def bubble(a,l):
    n=len(a)
    for i in range(n-1):
        flag=True
        for j in range(n-1-i):
            if l[j]>l[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                l[j],l[j+1]=l[j+1],l[j]
                flag=False
        if flag:
            break
    return a    
a=[[4,13,12],[8,10,5],[7,9,20],[16,8,3]]
print(bubble(a,findprime(a)))
