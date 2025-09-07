#PRIME CHECK
def isPrime(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return "Number is not prime"
    if m>200:
        return "Prime Greater than 200"
    return "Prime less than 200"


if __name__=='__main__':
    num=int(input("Enter a number: "))
    print(isPrime(num))
