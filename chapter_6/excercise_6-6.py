favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

should_take = ['jen', 'edward', 'george', 'deb', 'molly']

for i in should_take:
    if i in favorite_languages:
        print(i.title() + ', thank you for taking the survey')
    else:
        print(i.title() + " please take the survey!")