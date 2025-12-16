odd_numbers = [value for value in range(1, 20, 2)]

print("the first three values are: " + str(odd_numbers[0:3]))

#calculate the middle value in the list regardless of the length
middle_index = len(odd_numbers)//2
#use the middle index to subtract one to get the starting value
#and add two to get the end value (not one becuase of off-by-one index error)
print("three values from the middle are: " + str(odd_numbers[middle_index - 1 : middle_index + 2]))

print("the last three values are: " + str(odd_numbers[-3:]))