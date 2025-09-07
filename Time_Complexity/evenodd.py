def evenoddUsingAnd(num):
    if num&1:
        return "Odd"
    else:
        return "Even"

def evenOddUsingXor(num):
    if num^1<num:
        return "Odd"
    else:
        return "Even"

print(evenoddUsingAnd(1))
print(evenOddUsingXor(110))