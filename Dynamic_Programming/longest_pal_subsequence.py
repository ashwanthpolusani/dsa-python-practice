# given a string .
# find the length of longest possible subsequence

def longestSubsequence(s):
    i=0
    j=len(s)-1
    c=0
    r=""
    x=True
    while i<=j:
        if s[i]==s[j]:
            if i==j:
                c+=1
                r=r+s[i]+r[::-1]
                break
            else:
                c+=2
                r+=s[i]
            i+=1
            j-=1
        else:
            if x:
                j-=1
                x=False
            else:
                i+=1
                j+=1
                x=True
    print(c)
    return r if len(r)%2==1 else r+r[::-1]

s="acdaoaiefwoeuaa"
print(longestSubsequence(s))