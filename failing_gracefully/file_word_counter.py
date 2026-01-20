def CountFileWords(filename, word):
    try:
        with open(filename, 'r', encoding = 'UTF-8') as file_object:
            text_str = file_object.read()
    except FileNotFoundError:
        print('Sorry, the file could not be found.')
    else:
        print(text_str.count(str(word)))