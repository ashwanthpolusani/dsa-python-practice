#count all the prime numbers in alist using recurssion
l=[13,17,21,23,22,7,29]

def isprime(num,m=2):
    if m==int(num**(0.5))+1:
        return True
    if num%m==0:
        return False
    return isprime(num,m+1)

def primecheck(l,i):
    if i==len(l):
        return 0
    if isprime(l[i]):
        print(l[i])
        return primecheck(l,i+1)+1
    return primecheck(l,i+1)

print(primecheck(l,0))
# print(isprime(11,6))
