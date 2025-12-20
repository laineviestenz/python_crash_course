def make_shirt(size = 'large', message = 'I love Python'):
    print('A ' + size.lower() + ' t-shirt with "' + message + '" printed on it.')

make_shirt()
make_shirt('medium')
make_shirt(message = 'I love C++')