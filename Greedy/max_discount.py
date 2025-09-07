# Given a list of discounts for consecutive days, and an integer k,
# find the maximum total discount that can be obtained by selecting any k consecutive days.
# Sliding window approach
# Time complexity: O(n)
# Space complexity: O(1)

def maxDiscount(discounts, window):
    max_sum = 0
    curr_sum = 0
    # Calculate sum of first 'window' discounts
    for i in range(window):
        curr_sum += discounts[i]
    max_sum = curr_sum
    # Slide the window through the list and update the sums
    for i in range(window, len(discounts)):
        curr_sum += discounts[i]
        curr_sum -= discounts[i - window]
        max_sum = max(curr_sum, max_sum)
    return max_sum

discounts = [200, 1, 1, 1, 1, 3, 1, 1, 4, 2, 6, 7, 1000]
window = 5
print(maxDiscount(discounts, window))