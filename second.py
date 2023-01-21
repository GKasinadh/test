def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("Enter a number :"))

if is_prime(num) == True:
    print(num, "is a prime number")
    print(reverse_number(num))
else:
    print(num, "is not a prime number")






