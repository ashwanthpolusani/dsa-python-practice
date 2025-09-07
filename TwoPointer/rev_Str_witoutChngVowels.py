# Given a string .Reverse the string without changing the position of vowels
def revString(s):
    vowels = set("AEIOUaeiou")
    chars = list(s)
    left ,right = 0,len(chars) - 1
    while left <= right:
        if chars[left] in vowels and chars[right] in vowels:
            left += 1
            right -= 1
        elif chars[left] in vowels:
            left += 1
        elif chars[right] in vowels:
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)


s="hippopotamus"
print(revString(s))