def factorial(n):
    if n==1:
        return 1
    else: 
        return n*factorial(n-1)
num = int(input("Enter a number : "))
print("the factorial of ", num ,"is", factorial(num))

x = int(factorial(num))

print(x*num)
