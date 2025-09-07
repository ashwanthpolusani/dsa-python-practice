# Question: Find the largest minimum distance possible between C cows placed in N stalls
# Example: For stalls at positions [1,2,8,4,9] and 3 cows, answer is 3

def place_cows(stalls, cows):
    stalls.sort()
    
    def can_place_cows(distance):
        count = 1
        last_pos = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= distance:
                count += 1
                last_pos = stalls[i]
            if count == cows:
                return True
        return False

    left, right = 0, stalls[-1] - stalls[0]
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Test case
stalls = [1, 2, 8, 4, 9]
cows = 3
print(f"Maximum minimum distance: {place_cows(stalls, cows)}")