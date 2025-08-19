#Exercise

number=10
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative")   

#2
# number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#3
score = 80
if score >= 90:
    grade = "A"
elif score <= 80:
    grade= "B" 
elif score <= 65:
    grade= "C"
else:
    grade= "F"
print(f"Your grade is {grade}")    

#4
# ternary operator: similar to that of if,else with conditions
Number = 10
result="even" if Number/2 == 4 else "odd"
print(f"the number is {result}")

#5
num1 = 10
num2 = 5
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")
