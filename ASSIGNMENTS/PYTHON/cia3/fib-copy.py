import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

n = int(input("N: "))

for i in range(n+1):
    if (isFibonacci(i) == True and i == n):
        print(i, "is a Fibonacci Number")
        print("yes")
    elif(isFibonacci(i) != True and i == n):
        print(i, "is a not Fibonacci Number ")
