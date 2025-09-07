#count the frequency of same consequent letters followed by their frequency(aaabbbaacc===a3b3a2c2)
def find(s):
    ns=""
    c=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c+=1
        else:
            ns=ns+s[i]+str(c)
            c=1
    ns=ns+s[-1]+str(c)
    return ns
s="aaabbaaaacccddeff"
s2="abbacbababc"
print(find(s))
print(s2)
print(find(s2))