from die import Die
#create a D6
die = Die()
results = []

for roll_number in range(999999999):
    result = die.roll()
    results.append(result)

#analyze results
frequencies=[]
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)