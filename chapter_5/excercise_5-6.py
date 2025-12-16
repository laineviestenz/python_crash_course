# This is a program to determine a persons stage in life.
# If they are less than 2, they are a baby
# If they are 2-4, they are a toddler
# If they are 4-13, they are a a kid
# If they are 13-20 they are a teen
# If they are 20-65 they are an adult
# If they are over 65 they are an elder
# note that the upper bound of each age is not inclusive

def stage_of_life (age):
    #a function that takes the variable age and returns stage of life as a
    #string
    if age < 2:
        stage = "baby"
    elif age < 4:
        stage = "toddler"
    elif age < 13:
        stage = "kid"
    elif age < 20:
        stage = "teen"
    elif age < 65:
        stage = "adult"
    elif age >= 65:
        stage = "elder"
    return stage

print(stage_of_life(20))