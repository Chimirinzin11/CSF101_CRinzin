age=19
age_convert=str(age)
message="I am " + age_convert + " years old."
print(message)

#2

age="19"
age_int=int(age)
print(age_int)

#3
age=19
age=float(age)
print(age)

#4
non_num_str = "Hello"
try:
    non_num_int = int(non_num_str)
    print(non_num_int)
except ValueError as e:
    print(f"Error: {e}")
