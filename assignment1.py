#Question No. 1
'''Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included). The numbers should be printed on the output screen.
(Bonus point if you can print all the numbers on a single line)'''
a = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print(*a, sep=',')

#Question No. 2
'''Write a program that can compute the factorial of a given number. The number whose factorial is to be
computed is input from the keyboard.'''

n = int(input("Enter a non-negative integer: "))

if n >= 0:
    factorial = 1
    for i in range(2, n+1):
        factorial *= i

    print(f"The factorial of {n} is {factorial}.")
else:
    print("Invalid input. Please enter a non-negative integer.")

'''With a program to take as an input an integer number n, and generate a dictionary that contains (i, i*i)
where “i” lies between 1 and n (both included). The program should then print the dictionary.'''

def dict(n):
    my_dict = {}
    for i in range(1, n + 1):
        my_dict[i] = i ** 2
    return my_dict

a=dict(6)
print(a)

'''Write a program that can accept two strings as input and print the string with maximum length as an
output. If two strings have the same length, then the program should print both the strings.'''

a=str(input('First String : '))
b=str(input('Second String : '))

if len(a)<len(b):
    print(b)

elif len(b)<len(a):
    print(a)

else:
    print(a)
    print(b)

'''Write a program which can produce a dictionary where the keys are numbers between 1 and 20 (both
included) and the values are the square of keys. The program should print the values only.'''
x=1
for x in range(1, 21):
    d={x: x**2}
    x+=1
    print(d)

'''Write a program which can generate and print a list where the values are square of numbers between 1 and
20 (both included).'''
x=1
for x in range(1,21):
    y=x**2
    x+=1
    print(y)

'''Write a program which can generate a list where the values are square of numbers between 1 and 20
(inclusive). The program should only print the last 5 elements of the list.'''

x=[i**2 for i in range(1,21)]
print(x[-5:])

'''Write a program to convert Celsius (C) values into Fahrenheit (F). The program should ask for Celsius
value from the user and print the Fahrenheit value as an output.

Formula to Convert Celsius o Fahrenheit: [ F = C * ( 9 / 5 ) + 32 ]'''

temp_in_cel=float(input("Enter Temperature in Celsius : "))
temp_in_fahren= temp_in_cel*(9/5)+32
print("Temperature in Fahrenheit is ",temp_in_fahren)

'''Write a program which accepts a string as input from the keyboard. If the input string is "even" or
"EVEN" or "Even", print the even numbers from the list (my_numbers) given below. If the string is "odd" or
"ODD" or "Odd", print the odd numbers from the list. Otherwise simply print “Unknown Input!”'''

my_numbers = [7, 2, 4, 11, 19, 24, 66, 1, 42, 22, 37, 5, 3, 92, 73]
user_string = str(input("Enter even or odd"))
if user_string=='even' or 'EVEN' or 'Even':
    print([num for num in my_numbers if num % 2 == 0])
elif user_string=='odd' or 'ODD' or 'Odd':
    print([num for num in my_numbers if num%2 !=0])
else:
    print ('Unknown Input!')


'''Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of
the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and
five print “Fizz Buzz”.'''    
x=1
for i in range(1,21):
    if i%3==0 and i%5!=0:
        print("Buzz")
    elif i%5==0 and i%3!=0:
        print("Fizz")
    elif i%3==0 and i%5==0:
        print("Buzz Fizz")
    else:
        print(i)
        
            
