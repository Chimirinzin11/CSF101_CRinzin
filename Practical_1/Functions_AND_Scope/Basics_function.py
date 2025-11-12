#1
def greet():
    print("Hello, World!")
greet()    

#2
def greet(name):
    print(f"Hello, {name}!")
greet("Sonam") 

#3
def square(num):
    return num ** 2
result=square(10)
print(result)

#4
def is_even(n):
   return n % 2==0
print(is_even(4))  
print(is_even(9))      

#5
def prints_num(n):
    for i in range (1,n+1):
        print(i)
result=prints_num(9)        

