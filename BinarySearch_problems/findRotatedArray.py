#given an ascending order rotated array find the index of first element
#ip:[15,18,20,22,2,5,8,10,12,13]
a=[15,18,54,23,2,5,8,10,12,13]
def rotate(a):
    l = 0
    r = len(a) - 1
    while l < r:
        m = (l + r) // 2
        if a[m] > a[r]:
            l = m + 1
        else:
            r = m
    return a[l] 
print(rotate(a))