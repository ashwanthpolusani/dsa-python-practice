# given a string . find the longest palindromic substring and the count of palindromes in the string 
def longestSubstring(s):
    m=0
    start=None
    palCount=0
    for i in range(len(s)):
        l=i
        r=i
        while l>=0 and r<len(s) and s[l]==s[r]:
            #m=max(m,r-l+1)
            if r-l+1>m:
                m=r-l+1
                start=l
            l-=1
            r+=1
            palCount+=1
        l=i
        r=i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            #m=max(m,r-l+1)
            if r-l+1>m:
                m=r-l+1
                start=l
            l-=1
            r+=1
            palCount+=1
    print(f"The count of palindromes = {palCount}")
    return s[start:start+m]
s="ababba"
print(longestSubstring(s))