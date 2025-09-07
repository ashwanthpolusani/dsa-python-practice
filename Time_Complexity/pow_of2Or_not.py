#check wheather if a number is power of two or not(2^n):

#Time complexity == O(log n)
def findpow(n):
    i=1
    while 2**i<=n:
        if 2**i==n:
            return True
        i=i+1
    return False

#Time complexity == O(log n)
def findpow3(n):
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            return False
    return True

#Time complexity ==O (1)
def findpow1(n):
    return True if  n&(n-1)==0  else False

if __name__=='__main__':
    n=int(input("Enter a number: "))
    print(findpow(n))
    print(findpow1(n))