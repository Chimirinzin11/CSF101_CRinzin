
#Q1
length=int(input("Enter length: "))
width =int(input("Enter width: "))
area = length*width
print(f"Area of rectangle is: {area}") 

#  "OR"
def area(a,b):
    return a*b
print(area(10,10))

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
print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
print("Choose any one from above (1-2")
while True:
  x=int(input("Enter the number you want to convert: "))
  if x==1:
      celsius = float(input("Enter temperature in Celsius: "))
      conv= (celsius + 9/5)+32
      print(f"The temperature is {conv} Fahren")
  elif x==2:
      faren=float(input("Enter the fahren to convert: "))
      cov= (faren- 32) * 5/9
      print(f"The temperature is {cov} Celsius\n")
  else:
      print("error")    
