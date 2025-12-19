python_words = {
    "variable": 'a value placeholder', 
    "touple": "a list that cannot be modified without overwriting the value",
    "list": "an iterable list of values",
    "dictionary": "holds values for keywords",
    "laptop": "the device I use to write code"
    }

python_words.update({
    "hair": "what I'm losing",
    'for': "iterates to find value and exectues if its there",
    'print': 'displays the output',
    'python': ' a high level language'
})
#OLD WAY:
# for i in python_words:
#     print(i.title() + ": " + python_words[i])

#NEW WAY
for word, definition in python_words.items():
    print (word.title() + ": " + definition)
