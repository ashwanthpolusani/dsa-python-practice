# Question: Find all combinations from an array that sum up to a target value
# Example: Find combinations that sum to 15 from the array [3,6,8,2,6,5,7]

from itertools import combinations

def find_sum_combinations(arr, target):
    arr.sort()
    result = []
    for length in range(1, len(arr)):
        for combo in combinations(arr, length):
            if sum(combo) == target:
                result.append(list(combo))
    return result

# Test case
numbers = [3, 6, 8, 2, 6, 5, 7]
target_sum = 15
print(f"Combinations summing to {target_sum}: {find_sum_combinations(numbers, target_sum)}")
