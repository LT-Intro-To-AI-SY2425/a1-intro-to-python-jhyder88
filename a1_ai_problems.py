#Simple Calculator
# Write a Python program that takes two numbers as input from the user and prints their sum, difference, product, and quotient.
number = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
sum = number + number2
diff = number - number2
product = number * number2
if number != 0:
    quotient = number / number2
else:
    quotient = "undefined"
#Needed to the ChatGPT explaination in order to get the answer for quotient
print("Sum:" + sum)
print("Difference:" + diff)
print("Product:" + product)
print("Quotient" + quotient)

#Simple Temperature Converter
#Write a Python program that converts a temperature from Celsius to Fahrenheit and vice versa. The program should prompt the user to choose the conversion type and then input the temperature they wish to convert.
user_input = input("Would you like to convert from Celsius to Fahrenheit or Fahrenheit to Celsius")
if user_input == "Celsius":
    celsius = input("Temp in Celsius:")
    fahrenheit = celsius * 9/5 + 32
    print(celsius + "degrees celsius equals" + fahrenheit + "degrees fahrenheit")
elif user_input == "Fahrenheit":
    fahrenheit = input("Temp in Fahrenheit:")
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit + "degrees fahrenheit equals" + celsius + "degrees celsius")
#Struggled initally to figure out how to start, eventually got it but still not sure if parts of the conditional work

#Write a program that asks the user for their name and their birth year. Then, the program should calculate and print the year in which the user will turn 100 years old.
name = input("What is your name?")
year = input(int("What year were you born?"))
one_hundred = year + 100
print(name + "will turn 100 years old in the year" + one_hundred)




def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

