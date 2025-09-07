# find the juction point where two sorted arrays meet.

def find_junction_point(a):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        print(f"l= {l}, r= {r} , mid ={mid}")
        if a[l] > a[mid]:
            print("f{a[l]} > {a[mid]}")
            print("right",a[l:r+1])
            r = mid - 1
        else:
            print("f{a[l]} <= {a[mid]}")
            print("left",a[l:r+1])
            l = mid + 1
    return l

# Example usage:
a = [15, 18, 20, 22, 24,25,56, 1, 2, 5, 8, 10, 12, 13]
print(find_junction_point(a))