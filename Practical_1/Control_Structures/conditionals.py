#Exercise

number = 10
if number > 0:
    print("Number is positive")
else:
    print("number is negative")   


#2
num = -1
if num>0:
    print("The number is positive")
elif num<0:
    print("The  number is Negative ") 
else:
    print("The number is Zero")    

#3
score = 5
if  score>90:
    grade="A+"   
elif score>= 80:
    grade="A"
elif score>70:
    grade="B"
elif score>60:
    grade="c"  
else:
    grade="Fail"  
print(f"Your grade is : {grade}") 

#3 Ternary number (if.else)
Num=5
Num="Even" if Num%2==0 else "odd"
print(f"Result is : {Num}")

#Simple Calculator 
num1=50
num2=25
operator = "//"
if operator == "+":
    result=num1 + num2
elif operator =="-":
    result=num1-num2
elif operator == "/":
    result=num1/num2
elif operator=="*":
    result=num1*num2
else:
    result="Wrong operator" 
print(f"Result: {result}")                   