#1
x=10          #Global Scope  
def print_x():
    x=20
    print(f"Local scope: {x}")
print_x()
print(x)    #Global Scope

#2
count = 0

def increment():
    global count
    count += 1
    print(f"Count: {count}")

increment()
increment()
print(f"Final count: {count}")

#3
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner x: {x}")

    inner()
    print(f"Outer x: {x}")

outer()
