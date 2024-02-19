                    #PART 1
'''The perimeter of a rectangle with length 9 & width 7 '''
def perimeter(x,y):
    per=2*(x+y)
    return per

print("The perimeter with the length 9 and width 7 is",perimeter(9,7))

'''Your name stored as a variable'''
x='Aryan Guragain'
#using the defined variable in a function
def greetings(name):
    print("Hello! My name is",name)

greetings(x)

'''Print Python is great, its wild!'''
print("Python is great, its wild!")

'''The difference between Beth’s age (57) and Tom’s (34) '''
beth_age=57
tom_age=39
diff=beth_age-tom_age

print("The different between Beth's age",[beth_age],"and Tom's age",[tom_age],"is",diff)

''' 2 to the 10th power '''
def calc_power(x):
    pow=2**x
    print(pow)

calc_power(10)

'''7 factorial minus 5 factorial '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_of_seven = factorial(7)
factorial_of_five = factorial(5)

diff_of_factorials = factorial_of_seven - factorial_of_five
print("The difference between 7! and 5! is:", diff_of_factorials)

'''Your forename multiplied by 5'''
my_forename="Aryan"*5
print(my_forename)

'''  Your name left justified 15 spaces '''
name = "Aryan Guragain"
justified_name = name.ljust(15)
print(justified_name)

''' PI to 5 decimal places '''
import math

pi_to_five_decimal_places = round(math.pi, 5)

print(pi_to_five_decimal_places)

''' A variable named def that stores the number 7 '''
def=7
print(def)

'''200 modulus 12'''
x=200%12
print(x)

#7.2 as an integer value
decimal_value=7.2
whole_part=int(decimal_value)
print(whole_part)

#The unicode encoding for your name
a = "Aryan Guragain"

# Unicode encoding
unicodename = [ord(char) for char in a]

# Display the result
print(f"Original Name: {a}")
print("Unicode Encoded:")
for char, code in zip(a, unicodename):
    print(f"{char}: {code}")

                                #PART 2
    '''1. Write a Python program that prompts the user for two integer values and displays the results
of the first number divided by the second, with exactly two decimal places displayed.'''

first_num=int(input("enter a number: "))
second_num=int(input("Enter another number: "))
result=first_num/second_num
rounded_off_result=round(result,2)
print("The quotient is", rounded_off_result)

'''2. Write a Python program that prompts the user for two floating-point values and displays the
results of the first number divided by the second, with exactly two decimal places displayed. '''

a=float(input("Enter a number:"))
b=float(input("Enter another number:"))
result=a/b
rounded_off_result=round(result,2)
print("The result is ", rounded_off_result)

'''3.Write a Python program that prompts the user for two floating-point values and displays the 
results of the first number divided by the second, with exactly two decimal places displayed in 
scientific notation.  '''

num1=float(input("Enter first float number :"))
num2=float(input("Enter second float number :"))

#Calculate the result of first number divided by second
division_result=num1/num2

#Convert the division result to scientific notation
sci_notation=format(division_result,"0.2e")
print("The result is", sci_notation)

'''4. Write a Python program that prompts the user to enter a UTF-8 value between 32 and 126, 
and displays the corresponding character'''
utfvalue = int(input("Enter a UTF-8 value between 32 and 126: "))

# Check if the entered value is within the valid range
if 32 <= utfvalue <= 126:
    # Convert the UTF-8 value to a character
    character = chr(utfvalue)

    # Display the result
    print("The corresponding character for UTF-8 value of",{utfvalue}, "is:",{character})
else:
    print("Invalid input. Please enter a UTF-8 value between 32 and 126.")


                            #PART 3.Define a function, 
''' squared that take an integer and returns the value squared.'''

def get_sqr(num):
    result=num **2
    return result

a=int(input("ENTER  A NUMBER: "))
print(get_sqr(a))

'''print_ast that takes an integer value n and a string value symbol, with a default value of "*".
This character should be printed n times to the console.
'''

def print_ast(n):
    result= "*"*n
    print(result)

a=int(input("Enter the number of times you want to print *:"))
symbol=input("Enter the symbol (default is '*'):")
if not symbol:
    symbol="*"
print_ast(a)

'''Create a function that prompts the user for two integer values and displays the results of the
first number divided by the second to two decimal places.'''
def div_two():
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result=num1/num2
    rounded_of_result=round(result,2)
    print(rounded_of_result)

div_two()


