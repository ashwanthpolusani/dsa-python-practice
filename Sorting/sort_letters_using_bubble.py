# write a program for most efficient bubble sort

def bubble(a):
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

a=['c','e','a','b','f']
print(bubble(a))