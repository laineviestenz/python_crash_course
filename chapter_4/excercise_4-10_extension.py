odd_numbers = [value for value in range(1, 200, 2)]

#create a fundtion that finds the middle three values and returns it as a
#string that can be used in the print statement
def middle_3_values(num_list):
    #find the middle of the list (round down if not int)
    middle = len(num_list)//2
    #creates a string of the three middle values
    middle_three = str(num_list[middle - 1 : middle + 2])
    return middle_three
print("the first three values are: " + str(odd_numbers[0:3]))

print("three values from the middle are: " + middle_3_values(odd_numbers))

print("the last three values are: " + str(odd_numbers[-3:]))