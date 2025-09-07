# Given a string. Find the longest substring with non repeting characters
# using diactionary and idexes of chars as values
s="abcdaecyz"
def substr(s):
    res={}
    l=0
    r=0
    c=0
    while r<len(s):
        if s[r] not in res:
            res[s[r]]=r
        else:
            if res[s[r]]>=l:
                l=res[s[r]]+1
            res[s[r]]=r
        c=max(c,r-l+1)
        r+=1
    print(s[l:r])
    return c
print(substr(s))
        