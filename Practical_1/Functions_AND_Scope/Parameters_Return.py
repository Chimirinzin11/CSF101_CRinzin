#1 
def greet_with_default(name="Guest") :
    print(f"Hello, How are you doing? {name}")
greet_with_default() 
greet_with_default("Ronaldo")   
greet_with_default("Sonam")

#2
def calculate_rectangle_area(width, length):
    return width*length
area=calculate_rectangle_area(10,100)
print(f"The Area of this rectangle is : {area}")

#3
def print_info(**Cont):
    for key, value in Cont.items():
        print(f"{key} : {value}")
print_info(name="chimi", Height=181, Gender="MAlE")        

#4
def min_max(N):
    return min(N), max(N)
result=min_max([1,2,3,4,5,6,7,8,9,100])
print(f"min={result[0]} and max={result[1]}")

#5
def save_drive(a,b):
    if b==0:
        return "error"
    return a/b
print(save_drive(10,0))