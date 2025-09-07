# Take a sentence from user and sort the sentence according to the word length

s="An apple a day keeps the doctor away"
s=s.split()
l=[len(a) for a in s]
for i in range(len(s)):
    flag=True
    for j in range(len(s)-1-i):
        if l[j]>l[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
            l[j],l[j+1]=l[j+1],l[j]
            flag=False
    if flag:
        break
print(*s)