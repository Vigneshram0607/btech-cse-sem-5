import math


# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

n = int(input("N: "))

# A utility function to test above functions
for i in range(n+1):
    if (isFibonacci(i) == True and i == n):
        print(i, "is a Fibonacci Number")
    elif(isFibonacci(i) != True and i == n):
        print(i, "is a not Fibonacci Number ")