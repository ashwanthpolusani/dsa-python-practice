#Find peak Element in the sorted and rotated array

def peak_ele(a):
    l=0
    r=len(a)-1
    while l<r:
        m=(l+r)//2
        if a[m]>a[r]:
            l=m+1 
        else:
            r=m
        print("loper")
    return a[l-1]   

a=[18,19,20,21,2,3,4,5,6,7,8,9,10,11]
print(peak_ele(a))