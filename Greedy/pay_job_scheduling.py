def max_pay_schedule(time, pay):
    for i in range(len(pay)):
        temp = pay[i]
        for j in range(i):
            if time[i][0] >= time[j][1]:
                temp = max(temp, pay[j] + pay[i])
        pay[i] = temp
    return pay

def max_pay_schedule1(time, pay):
    dp=[0]*len(pay)
    for i in range(len(pay)):
        dp[i] = pay[i]
        for j in range(i): 
            if time[i][0] >= time[j][1]:
                dp[i] = max(dp[i], dp[j] + pay[i])
    return dp

time = [(1,2),(2,5),(4,6),(6,7),(5,8),(7,9)]
pay = [5,6,5,4,11,2]
result = max_pay_schedule1(time, pay)
print(result)

result = max_pay_schedule(time, pay)
print(result)
