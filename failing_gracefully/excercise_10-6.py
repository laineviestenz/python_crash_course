print("Enter two numbers to add together: ")

a = input("Enter the first number: ")
b = input('Enter the second number: ')

try:
    answer = int(a) + int(b)
except ValueError:
    print("please provide a valid input")
else:
    print(answer)