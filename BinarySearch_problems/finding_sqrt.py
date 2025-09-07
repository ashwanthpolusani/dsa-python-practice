# Find the square root of a number. 


def integer_sqrt(num):
    l = 1
    r = num // 2
    while l <= r:
        mid = (l + r) // 2
        print(f"l= {l}, r= {r} , mid ={mid}")
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
    return r

print(integer_sqrt(35))