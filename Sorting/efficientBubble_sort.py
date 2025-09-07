# write a program for most efficient bubble sort
a=[88,21,3,32,43,4,17,-1,14,8,5,14]
n=len(a)
for i in range(n-1):
    flag=True
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            flag=False
    print(a)
    if flag:
        break