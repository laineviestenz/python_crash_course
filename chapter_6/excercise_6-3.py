python_words = {
    "variable": 'a value placeholder', 
    "touple": "a list that cannot be modified without overwriting the value",
    "list": "an iterable list of values",
    "dictionary": "holds values for keywords",
    "laptop": "the device I use to write code"
    }

for i in python_words:
    print(i.title() + ": " + python_words[i])