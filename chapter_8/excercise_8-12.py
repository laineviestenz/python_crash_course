def sandwich_order(*toppings):
    #check if there is only one item, cycle through list to print
    if len(toppings) > 1:
        print('A sandwich with ', end = '')
        for topping in toppings[0:-1]:    
            print(topping, end = ', ')
        #the last item should be preceded with an 'and' not a comma, and should have a '.'
        print('and ' + toppings[-1] + '.')
    #if theres only one item print:
    else:
        print("A sandwich with only " + toppings[0] + '.')
   

sandwich_order('peperoni', 'mayo', 'salt')

sandwich_order('sausage')

sandwich_order('ham', 'turkey', 'mayo', 'lettus', 'tomatoes', 'pickles')

#this doesn't work and I don't think I have learned how to fix it
#leaving because I may revisit it to clean up this code a little
# print('A sandwich with: ' + str(topping for topping in toppings) + '.')