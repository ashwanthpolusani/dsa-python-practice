# Finding kth largest element using bubble sort

def bubble(a,k):
    n=len(a)
    for i in range(k):
        flag=True
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=False
        print(a)
        if flag:
            break
    return a[n-k]
a=[1,2,3,4,5,6,7,8,9,10]
a.reverse()
print(bubble(a,4))