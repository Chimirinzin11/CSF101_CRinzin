#1
def factorial(n):
    if n==0:
        return 1
    else:
        return (n*factorial(n-1))
print(factorial(5))        

#2
def factorial(n):
    if n <=1:
        return n
    else:
        return factorial(n-1) + factorial (n-2)
print(factorial(7))    