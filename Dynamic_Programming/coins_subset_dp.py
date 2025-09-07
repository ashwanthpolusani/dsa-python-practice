def is_sum_possible(a, amt):
    if amt>sum(a):
        return 0
    dp = [[0] * (amt + 1) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(2, amt + 1):
            if j == 0 or j == a[i]:
                dp[i][j] = 1
            else:
                if i > 0 and (dp[i - 1][j] or (j - a[i] >= 0 and dp[i - 1][j - a[i]])):
                    dp[i][j] = 1 
    return dp[-1][-1] == 1

def min_coins_req(a, amt):
    if amt>sum(a):
        return "Not Possible"
    dp = [[0] * (amt + 1) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(amt + 1):
            if j == a[i]:
                dp[i][j] = 1
            elif i>0 and j<a[i]:
                dp[i][j]=dp[i-1][j]
            else:
                if i>0 and  j - a[i] >= 0 and dp[i - 1][j - a[i]]:
                    dp[i][j] = dp[i-1][j-a[i]]+1
                elif i > 0 and (dp[i - 1][j]):
                    dp[i][j] = dp[i-1][j]
    for i in dp:
        print(i)
    return f"{dp[-1][-1]} coins reqiured" if dp[-1][-1] else "Not Possible"


# Example usage:
a = [2,3,5,9]
a.sort()
amt = 10
print("Possible" if is_sum_possible(a, amt) else "Not possible")
print( min_coins_req(a, amt))
