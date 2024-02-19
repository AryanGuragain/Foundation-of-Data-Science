def addition(a,b):
    sum=a+b
    print(sum)

def subtraction(a,b):
    difference=a-b
    print (difference)

def  multiplication(a,b):
    product=a*b
    print(product)

def division(a,b):
    quotient=a/b
    print(quotient)

def modulus(a,b):
    mod=a%b
    print(mod)

def trunkated_division(a,b):
    trunk_div=a//b
    print(trunk_div)

def power(base,exponent):
    result=base**exponent
    return result


x=int(input("Enter first number"))
y=int(input("Enter second number:"))
print("\nChoose operation")
print ("1.Addition")
print ("2.Substraction")
print ("3.Multiplication")
print ("4.Division")
print ("5.Modulus")
print ("6.Truncated Division")
print ("7.Power")

choice=int(input("Enter your choice"))

if choice==1:
    addition(x,y)

elif choice==2:
    subtraction(x,y)

elif choice==3:
    multiplication(x,y)

elif choice==4:
    division(x,y)

elif choice==5:
    modulus(x,y)

elif choice==6:
    trunkated_division(x,y)

elif choice==7:
    b=(int(input("Enter the base of the power:")))
    e=(int(input("Enter the exponent")))
    print (power(b,e))

else:
    print("Invalid choice. Please try again")




