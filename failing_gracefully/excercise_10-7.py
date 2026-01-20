print("Enter two numbers to add together: ")
print("Enter 'q' to end.")

while True:
    a = input("Enter the first number: ")
    if a == 'q':
        break
    b = input('Enter the second number: ')
    if b == 'q':
        break

    try:
        answer = int(a) + int(b)
    except ValueError:
        print("please provide a valid input")
    else:
        print(answer)