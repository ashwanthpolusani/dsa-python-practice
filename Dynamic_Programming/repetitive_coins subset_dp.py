def min_coins(coin, amt):
    dp = [0] * (amt + 1)
    for i in range(len(coin)):
        for j in range(coin[i], amt + 1):
            if j == coin[i]:
                dp[j] = 1
            if dp[j] and dp[j-coin[i]]:
                dp[j]=min(dp[j],1+dp[j-coin[i]])
            elif (dp[j-coin[i]]):
                dp[j]=dp[j-coin[i]]+1
    print([i for i in range(amt+1)])
    print(dp)
    return dp[-1]

coin = [2, 3, 4, 5]
amt = 13
print(min_coins(coin, amt))