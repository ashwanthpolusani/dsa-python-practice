def reverse(m):
    rev=0
    while m>0:
        x=m%10
        rev=rev*10+x
        m//=10
    print(rev)
def reverse1(m,re=0):
    if m<=0:
        return re
    x=m%10
    re=re*10+x
    return reverse1(m//10,re)
num=315
print(reverse1(315))