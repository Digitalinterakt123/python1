def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f

num = int(input("Enter a value : "))

fac = factorial(num)
print(fac)