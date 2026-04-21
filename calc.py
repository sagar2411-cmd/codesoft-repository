a = float(input("enter a number : "))
operator = input("enter the opeator :(+,-,*,/,%,per,avg) : ")
b = float(input("enter b number : "))

def sum(a,b):
    sum = a+b
    return sum

def substract(a,b):
    substract = a-b 
    return substract

def mul(a,b):
    mul = a*b
    return mul

def divide(a,b):
    divide = a/b
    return divide
if(a == 0):
    print("can't divided by zero")
elif(b == 0):
    print("can't divide by zero ")

def module(a,b):
    module = a%b
    return module   

def per(a,b):
    per = (a*b)/100
    return per 

def avg(a,b):
    avg = (a+b) / 2
    return avg
    
if(operator == "+"):
    print("THE SUM IS : ",sum(a,b))   
elif(operator == "-"):
    print("THE SUBSTRACT IS : ",substract(a,b))
elif(operator == "*"):
    print("THE MULTIPLY IS : ",mul(a,b))
elif(operator == "/"):
    print("THE DIVIDE IS : ",divide(a,b))
elif(operator == "%"):
    print("the module is : ",module(a,b))  
elif(operator == "per"):
    print("THE percentage IS : ",per(a,b)) 
elif(operator == "avg"):
    print("the avg is : ",avg(a,b))          
else:
    print("invalid opeartor")
