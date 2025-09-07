# Question: Given a number N, find the minimum number of operations to reach 1
# Operations allowed:
# 1. Subtract 1 from N
# 2. If N is divisible by 2, divide by 2
# 3. If N is divisible by 3, divide by 3

from collections import deque 

# Solution 1: Recursive approach
def solve_recursive(n):
    def count_steps(n, steps=0):
        if n < 1:
            return float('inf')
        if n == 1:
            return steps
        options = [count_steps(n-1, steps+1)]
        if n % 2 == 0:
            options.append(count_steps(n//2, steps+1))
        if n % 3 == 0:
            options.append(count_steps(n//3, steps+1))
        return min(options)
    return count_steps(n)

# Solution 2: BFS approach
def solve_bfs(n): 
    queue = deque([(n, 0)]) # (current number, operations count) 
    visited = set() # To avoid redundant calculations 
    while queue: 
        num, steps = queue.popleft() 
        if num == 1: 
            return steps 
        if num - 1 not in visited: 
            visited.add(num - 1) 
            queue.append((num - 1, steps + 1)) 
        if num % 2 == 0 and num // 2 not in visited: 
            visited.add(num // 2) 
            queue.append((num // 2, steps + 1)) 
        if num % 3 == 0 and num // 3 not in visited: 
            visited.add(num // 3) 
            queue.append((num // 3, steps + 1)) 

# Solution 3: Dynamic Programming approach
def solve_dp(n):
    dp=[0]*(n+1)
    for i in range(2,n+1):
        dp[i]=dp[i-1]+1
        if i%2==0:
            dp[i]=min(dp[i//2]+1,dp[i])
        if i%3==0:
            dp[i]=min(dp[i//3]+1,dp[i])
    return dp[n]

# Test cases
n = 10
print(f"Recursive solution: {solve_recursive(n)}")
print(f"BFS solution: {solve_bfs(n)}")
print(f"DP solution: {solve_dp(n)}")