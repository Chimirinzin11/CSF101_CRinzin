#Exercise
count=0
while True:
    print(count)
    count += 1
    if count >= 10:
        break
print("Completed")

#2
for num in range(1,10):
    if num% 2==0:
        continue
    print(num)

list=[1,2,3,4,5,6,7,8,9]
search = 7
for num in list:
    if num == search:
        print(f"found it {search}")
    else:
        (f"nope {search}")    


#Guess game
import random

guessed_num= random.randint(1,100)   
Total_guess =0
while True:

 guess=int(input("Guess a number from 1-100: "))
 Total_guess +=1

 if guess==guessed_num:
    print(f"Congratulation ,Guessed after {Total_guess} attempts")
    break
 elif guess <guessed_num:
     print("Too low")
 elif guess> guessed_num:
     print("too high")
 else:
     print("1-100")    



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 21
if is_prime(number):
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")
