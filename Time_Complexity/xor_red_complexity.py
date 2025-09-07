n=int(input("Enter the number: "))
s=1
for i in range(2,n+1):
    s=s^i
print(s)
def findxor(n): 
    return {0: n, 1: 1, 2: n + 1, 3: 0}[n % 4]
    
print(findxor(n))
