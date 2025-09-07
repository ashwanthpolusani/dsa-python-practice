m,n=map(int,input("Enter two numbes: ").split())
def findwhole(m,n):
    def findxor(n):
        return {0: n, 1: 1, 2: n + 1, 3: 0}[n % 4]
    return findxor(m-1)^findxor(n)
print(f"The xor of {m} to {n} ={findwhole(m,n)}")
