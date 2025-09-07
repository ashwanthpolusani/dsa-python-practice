from collections import Counter

#if single largest element exists
def max_freq_ele(arr,k=1):
    d=Counter(arr)
    m=0
    for i in d:
        if d[i]>m:
            m=d[i]
            res=i
    return res

#if multiple largest elements exists
def max_freq_ele(arr,k=1):
    d=Counter(arr)
    m=max(d.values())
    b=[]
    b=[[] for _ in range(m+1)]
    for i in d.items():
        b[i[1]].append(i[0])
    return b[-k]


arr=[2,13,4,2,9,9,3,5,8,7,13,3]
print(max_freq_ele(arr,1))
