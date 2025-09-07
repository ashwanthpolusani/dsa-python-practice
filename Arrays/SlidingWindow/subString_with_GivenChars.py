# Given a string. Find the longest substring with non repeting characters and has specific strings
# using diactionary and idexes of chars as values
a="abcdecfbge"

def substring(s,m,n):
    d={}
    r=0
    l=0
    mx=0
    while r<len(s):
        if s[r] not in d:
            d[s[r]]=r
        else:
            if d[s[r]]>=l:
                l=d[s[r]]+1
            d[s[r]]=r
        if r-l+1>mx and m in d and n in d and d[m]>=l and d[n]>=l:
            mx=r-l+1
            print(s[l:r+1])
        r+=1
    return mx
m='c'
n='d'
print(substring(a,m,n))  