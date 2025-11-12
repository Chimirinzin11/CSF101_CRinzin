
#Q1
length=int(input("Enter length: "))
width =int(input("Enter width: "))
area = length*width
print(f"Area of rectangle is: {area}") 

#Q2
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(5))

#Q3
x=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))
z=int(input("Enter number 3: "))
if x>=y and x>=z:
    print(f"The Largest number is: x")
if y>=x and y>=z:
    print(f"The Largest number is: y")
else:
    print(f"The Largest number is: z")   

#Q4
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")
    
   