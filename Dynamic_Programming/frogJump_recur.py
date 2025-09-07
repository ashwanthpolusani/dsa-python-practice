# given a  array of stones.
# Preform 1 or 2 jumps and find the minimum energy required by the frog to reach nth stone
arr=[10,20,30,70,30,20,10]

#recursion
def frogjump(n):
    if n<=1:
        return dp[n]
    dp[n]=min((frogjump(n-1)+abs(arr[n-1]-arr[n])),(frogjump(n-2)+abs(arr[n-2]-arr[n])))
    return dp[n]
dp=[0,abs(arr[1]-arr[0]),0,0,0,0,0]
frogjump(6)
print(dp)

#using varibles instead of tabulation
def frogjump2(a,n):
    n1=0
    n2=abs(a[1]-a[0])
    s=0
    for i in range(2,n+1):
        s=min(n1+abs(a[i]-a[i-2]),n2+abs(a[i]-a[i-1]))
        n1=n2
        n2=s
        print(s,end=" ")
    print()
frogjump2(arr,6)

# tabulation
def frogjump3(a,n):
    d=[0]*len(a)
    d[1]=abs(a[1]-a[0])
    for i in range(2,n+1):
        d[i]=min(d[i-2]+abs(a[i]-a[i-2]),d[i-1]+abs(a[i]-a[i-1]))
    print(d)
frogjump3(arr,6)

# tabulation with k frog jumps
def frogjump4(a,n,k):
    d=[0]*len(a)
    for i in range(1,k):
        d[i]=abs(a[i]-a[0])
    for i in range(2,n+1):
        mini=d[i-1]+abs(a[i]-a[i-1])
        for j in range(2,k+1):
            mini=min(mini,d[i-j]+abs(a[i]-a[i-j]))
        d[i]=mini
    print("Frog4",d)
frogjump4(arr,6,3)
