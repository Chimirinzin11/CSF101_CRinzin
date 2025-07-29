print("good morning")

def myfunc():
    x="meaning"
    print("show me the "+x )
myfunc()    

z="heart"
print(f"shape of my {z}")

c="chimi"
print(type(c))

x,y,z=1,2,3
print(x, y, z)

def myfunc():
    global x
    x = "changed meaning"

myfunc()  
print("evrythin is about a " + x)
