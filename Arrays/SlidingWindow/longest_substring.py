# Question: Find the length of the longest substring without repeating characters.
# Example: For string "abcdecfbge", find the longest substring without repeating characters.

def find_longest_substring(s):
    char_pos = {}
    start = 0
    max_length = 0
    
    for curr_pos, char in enumerate(s):
        if char in char_pos and char_pos[char] >= start:
            start = char_pos[char] + 1
        else:
            max_length = max(max_length, curr_pos - start + 1)
        char_pos[char] = curr_pos
        print(f"Current substring: {s[start:curr_pos+1]}")
    
    return max_length

test_string = "abcdecfbge"
print(f"Length of longest substring: {find_longest_substring(test_string)}")
