import time
from calculate import *

print(
    "Hello, I'm Jarvis, your personal calculator bot\n Please enter two numbers and an operator."
)

time.sleep(3)

number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

print("Calculating...")
time.sleep(2)

result = perform_calculation(number_one, number_two, operator)

print("The result is: " + str(result))
