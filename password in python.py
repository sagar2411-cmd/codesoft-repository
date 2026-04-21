import random
import string
length = int(input("enter length : "))

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ([random.choice(chars) for i in range(length)])

for i in range(length):
    password = random.choice(chars)
   
    
print("your random password is : ",password)
