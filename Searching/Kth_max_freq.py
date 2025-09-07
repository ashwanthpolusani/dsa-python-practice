# Given a array.
# Find the kth max highest frequency elements

from collections import Counter
def max_freq_ele(arr,k):
    d=Counter(arr)
    m=max(d.values())
    b=[]
    b=[[] for _ in range(m+1)]
    for i in d:
        b[d[i]].append(i)
    print(b)
    for i in range(len(b)-1,-1,-1):
        if b[i]!=[]:
            k-=1
        if k==0:
            return b[i]
    return "No Highest kth frequency"
arr=[2,13,4,10,2,9,3,3,3,8,9,3,5,8,5,6,2,2,3,4,6,3,5,23,5,2,5,7,13,3]
k=4
print(max_freq_ele(arr,k))